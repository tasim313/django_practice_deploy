from django import forms
from . import music_models


class album_form(forms.ModelForm):
    release_date = forms.DateTimeField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = music_models.album
        fields = '__all__'