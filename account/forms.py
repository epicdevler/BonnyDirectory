from django import forms
from listings.models import Listing


class ListingForm(forms.ModelForm):
    class Meta:
        model= Listing
        fields= ["name", "category", "email", "facebook", "website", "instagram", "description", "photo_main", "photo_1", "photo_2", "photo_3", "photo_4",
        "location", "phone_number", "opening_time", "closing_time"]

        widgets = {
            "name": forms.TextInput(attrs={'class': 'form-control'}),
            "category": forms.Select(attrs={'class': 'form-control'}),
            "email": forms.EmailInput(attrs={'class': 'form-control'}),
            "description": forms.Textarea(attrs={'class': 'form-control'}),
            "instagram": forms.TextInput(attrs={'class': 'form-control'}),
            "facebook": forms.TextInput(attrs={'class': 'form-control'}),
            "website": forms.TextInput(attrs={'class': 'form-control'}),
            "photo_main": forms.FileInput(attrs={'class': 'form-control'}),
            "photo_1": forms.FileInput(attrs={'class': 'form-control'}),
            "photo_2": forms.FileInput(attrs={'class': 'form-control'}),
            "photo_3": forms.FileInput(attrs={'class': 'form-control'}),
            "photo_4": forms.FileInput(attrs={'class': 'form-control'}),
            "location": forms.TextInput(attrs={'class': 'form-control'}),
            "phone_number": forms.NumberInput(attrs={'class': 'form-control'}),
            "opening_time": forms.TimeInput(attrs={'class': 'form-control'}),
            "closing_time": forms.TimeInput(attrs={'class': 'form-control'}),
        }