# myapp/forms.py
from django import forms
from .models import UploadedFile, SWMember


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadedFile
        fields = ['file']


class SWMemberForm(forms.ModelForm):
    class Meta:
        model = SWMember
        fields = '__all__'

