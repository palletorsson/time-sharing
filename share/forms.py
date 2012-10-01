from django import forms
from models import Share

class ShareForm(forms.ModelForm):
    class Meta:
        model = Share
        exclude = ('user', 'status',)  