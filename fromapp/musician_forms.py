from django import forms
from . import music_models


class musician_form(forms.ModelForm):
    class Meta:
        model = music_models.musicians
        fields = '__all__'