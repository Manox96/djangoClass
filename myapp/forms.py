from django import forms
from .models import Photo

class PhotoUploadForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['Nom', 'Descreption', 'image']
        labels = {
            'Nom': 'Nom de la photo',
            'Descreption': 'Description',
            'image': 'Image'
        }
        widgets = {
            'Descreption': forms.Textarea(attrs={'rows': 4}),
        } 