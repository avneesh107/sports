from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['gender', 'date_of_birth', 'mobile_number', 'college']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }
class MatchUploadForm(forms.Form):
    file = forms.FileField(label="Upload Excel File (.xlsx)")