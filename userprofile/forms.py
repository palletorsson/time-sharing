from django import forms
from models import Userprofile

class UserprofileForm(forms.ModelForm):
    class Meta:
        model = Userprofile
        exclude = ('user', 'status')
