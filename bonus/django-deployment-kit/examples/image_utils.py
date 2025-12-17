"""
Image processing utilities for media uploads.

Handles resizing, thumbnail generation, and format optimization.
Supports HEIC conversion and WebP output for better compression.
"""
import io
import os
from pathlib import Path

from django.core.files.base import ContentFile
from PIL import Image

# Try to import HEIC support
try:
    import pillow_heif
    pillow_heif.register_heif_opener()
    HAS_HEIF = True
except ImportError:
    HAS_HEIF = False

# Maximum dimensions for web display
MAX_WIDTH = 1920
MAX_HEIGHT = 1920

# WebP conversion setting (set to True for better compression)
CONVERT_TO_WEBP = True
WEBP_QUALITY = 85

# Thumbnail dimensions
THUMB_WIDTH = 300
THUMB_HEIGHT = 300

# JPEG quality for resized images
JPEG_QUALITY = 85


def process_uploaded_image(uploaded_file):
    """
    Process an uploaded image file.

    Resizes large images to web-appropriate dimensions.

    Args:
        uploaded_file: Django UploadedFile or similar file-like object

    Returns:
        dict with:
            - file: ContentFile with processed image (or original if not an image)
            - width: Image width (or None for non-images)
            - height: Image height (or None for non-images)
            - file_size: File size in bytes
            - is_resized: Whether image was resized
    """
    original_name = getattr(uploaded_file, 'name', 'image.jpg')
    ext = Path(original_name).suffix.lower()

    # Supported image extensions (HEIC requires pillow-heif)
    supported_exts = ['.jpg', '.jpeg', '.png', '.gif', '.webp']
    if HAS_HEIF:
        supported_exts.extend(['.heic', '.heif'])

    # Skip non-image files
    if ext not in supported_exts:
        return {
            'file': uploaded_file,
            'width': None,
            'height': None,
            'file_size': uploaded_file.size if hasattr(uploaded_file, 'size') else None,
            'is_resized': False,
        }

    try:
        uploaded_file.seek(0)
        img = Image.open(uploaded_file)

        # Handle GIFs separately (preserve animation)
        if ext == '.gif' and getattr(img, 'is_animated', False):
            uploaded_file.seek(0)
            return {
                'file': uploaded_file,
                'width': img.width,
                'height': img.height,
                'file_size': uploaded_file.size if hasattr(uploaded_file, 'size') else None,
                'is_resized': False,
            }

        original_width, original_height = img.size
        is_resized = False

        # Resize if larger than max dimensions
        if original_width > MAX_WIDTH or original_height > MAX_HEIGHT:
            img.thumbnail((MAX_WIDTH, MAX_HEIGHT), Image.Resampling.LANCZOS)
            is_resized = True

        # Convert RGBA to RGB for JPEG
        if img.mode in ('RGBA', 'P') and ext in ('.jpg', '.jpeg'):
            background = Image.new('RGB', img.size, (255, 255, 255))
            if img.mode == 'P':
                img = img.convert('RGBA')
            background.paste(img, mask=img.split()[3])
            img = background

        # Save to buffer - convert to WebP if enabled for better compression
        buffer = io.BytesIO()

        if CONVERT_TO_WEBP and ext != '.gif':
            # Convert to WebP for ~30-50% size reduction
            if img.mode == 'RGBA':
                img.save(buffer, format='WEBP', quality=WEBP_QUALITY, lossless=False)
            else:
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                img.save(buffer, format='WEBP', quality=WEBP_QUALITY)
            # Update filename to .webp
            output_name = str(Path(original_name).with_suffix('.webp'))
        elif ext in ('.jpg', '.jpeg'):
            img.save(buffer, format='JPEG', quality=JPEG_QUALITY, optimize=True)
            output_name = original_name
        elif ext == '.png':
            img.save(buffer, format='PNG', optimize=True)
            output_name = original_name
        elif ext == '.webp':
            img.save(buffer, format='WEBP', quality=JPEG_QUALITY)
            output_name = original_name
        elif ext == '.gif':
            img.save(buffer, format='GIF')
            output_name = original_name
        else:
            img.save(buffer, format='JPEG', quality=JPEG_QUALITY)
            output_name = original_name

        buffer.seek(0)
        content_file = ContentFile(buffer.read(), name=output_name)

        return {
            'file': content_file,
            'width': img.width,
            'height': img.height,
            'file_size': content_file.size,
            'is_resized': is_resized,
        }

    except Exception:
        # If processing fails, return original file
        uploaded_file.seek(0)
        return {
            'file': uploaded_file,
            'width': None,
            'height': None,
            'file_size': uploaded_file.size if hasattr(uploaded_file, 'size') else None,
            'is_resized': False,
        }


def generate_thumbnail(image_file, max_width=THUMB_WIDTH, max_height=THUMB_HEIGHT):
    """
    Generate a thumbnail for an image file.

    Args:
        image_file: Django FieldFile or file-like object
        max_width: Maximum thumbnail width
        max_height: Maximum thumbnail height

    Returns:
        ContentFile with thumbnail or None if generation fails
    """
    try:
        image_file.seek(0)
        img = Image.open(image_file)

        # Skip animated GIFs
        if getattr(img, 'is_animated', False):
            return None

        # Create thumbnail
        img.thumbnail((max_width, max_height), Image.Resampling.LANCZOS)

        # Convert to RGB if needed
        if img.mode in ('RGBA', 'P'):
            background = Image.new('RGB', img.size, (255, 255, 255))
            if img.mode == 'P':
                img = img.convert('RGBA')
            if img.mode == 'RGBA':
                background.paste(img, mask=img.split()[3])
            else:
                background.paste(img)
            img = background

        # Save as JPEG
        buffer = io.BytesIO()
        img.save(buffer, format='JPEG', quality=80, optimize=True)
        buffer.seek(0)

        # Generate filename
        original_name = getattr(image_file, 'name', 'image.jpg')
        base_name = Path(original_name).stem
        thumb_name = f"{base_name}_thumb.jpg"

        return ContentFile(buffer.read(), name=thumb_name)

    except Exception:
        return None


def get_image_dimensions(image_file):
    """
    Get dimensions of an image file.

    Args:
        image_file: File-like object

    Returns:
        Tuple of (width, height) or (None, None) if not an image
    """
    try:
        image_file.seek(0)
        img = Image.open(image_file)
        return img.width, img.height
    except Exception:
        return None, None
