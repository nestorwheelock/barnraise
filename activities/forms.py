from django import forms
from .models import Activity, Neighborhood


class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = [
            "title",
            "description",
            "neighborhood",
            "location_hint",
            "starts_at",
            "duration_minutes",
            "helpers_needed",
            "host_email",
            "host_phone",
        ]
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "What are you doing?",
            }),
            "description": forms.Textarea(attrs={
                "class": "form-textarea",
                "rows": 4,
                "placeholder": "Tell people more about what you're doing and what kind of help you need...",
            }),
            "neighborhood": forms.Select(attrs={
                "class": "form-select",
            }),
            "location_hint": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "Near 12th & Chicon, by the coffee shop",
            }),
            "starts_at": forms.DateTimeInput(attrs={
                "class": "form-input",
                "type": "datetime-local",
            }),
            "duration_minutes": forms.Select(attrs={
                "class": "form-select",
            }, choices=[
                (30, "About 30 minutes"),
                (60, "About 1 hour"),
                (90, "About 1.5 hours"),
                (120, "About 2 hours"),
                (180, "About 3 hours"),
                (240, "About 4 hours"),
            ]),
            "helpers_needed": forms.NumberInput(attrs={
                "class": "form-input",
                "min": 1,
                "max": 20,
            }),
            "host_email": forms.EmailInput(attrs={
                "class": "form-input",
                "placeholder": "your@email.com",
            }),
            "host_phone": forms.TextInput(attrs={
                "class": "form-input",
                "placeholder": "(optional)",
            }),
        }
        labels = {
            "title": "What are you doing?",
            "description": "Tell people more",
            "neighborhood": "Neighborhood",
            "location_hint": "Nearby landmark or cross streets",
            "starts_at": "When?",
            "duration_minutes": "How long? (roughly)",
            "helpers_needed": "How many helpers?",
            "host_email": "Your email (for updates)",
            "host_phone": "Your phone (optional)",
        }
