from django import forms
from .models import Photo

class PhotoUploadForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['Nom', 'Descreption', 'image', 'is_pulic']
        labels = {
            'Nom': 'Nom de la photo',
            'Descreption': 'Description',
            'image': 'Image',
            'is_pulic': 'Publique'
        }
        widgets = {
            'Descreption': forms.Textarea(attrs={'rows': 4}),
        } 