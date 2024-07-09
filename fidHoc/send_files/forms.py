# myapp/forms.py
from django import forms

class UploadForm(forms.Form):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    destination = forms.CharField(max_length=100)
    mode = forms.ChoiceField(choices=[('mode1', 'Mode 1'), ('mode2', 'Mode 2')])
    notes = forms.CharField(widget=forms.Textarea)

