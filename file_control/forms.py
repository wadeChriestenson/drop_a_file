from django import forms
from .models import userFiles


class FileForm(forms.ModelForm):
    class Meta:
        model = userFiles
        fields = ['file']
        labels = {'file': ''}
