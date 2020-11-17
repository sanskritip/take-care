from accounts.models import Bio
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Bio
        fields = ['firstname','lastname', 'displayimage','status']

    
