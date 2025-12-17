"""
Signals for automatic media optimization on upload.

Handles post_save signals to optimize images when they're uploaded.
"""
import logging
from pathlib import Path

from django.db.models.signals import pre_save
from django.dispatch import receiver

from .image_utils import process_uploaded_image

logger = logging.getLogger(__name__)


def optimize_image_field(instance, field_name):
    """
    Optimize an image field if it has changed.

    Args:
        instance: Model instance
        field_name: Name of the ImageField/FileField
    """
    field = getattr(instance, field_name, None)
    if not field:
        return

    # Check if this is a new file (not already saved)
    if not field.name:
        return

    # Skip if already a .webp file (already optimized)
    if field.name.endswith('.webp'):
        return

    # Check if file exists and is an image
    ext = Path(field.name).suffix.lower()
    if ext not in ('.jpg', '.jpeg', '.png', '.heic', '.heif', '.bmp', '.tiff'):
        return

    try:
        # Process the image
        result = process_uploaded_image(field.file)

        if result.get('file') and result['file'] != field.file:
            # Get new filename
            new_name = result['file'].name

            # Save optimized version
            field.save(new_name, result['file'], save=False)

            logger.info(f"Optimized {field_name}: {field.name} -> {new_name}")

    except Exception as e:
        logger.warning(f"Failed to optimize {field_name} for {instance}: {e}")
