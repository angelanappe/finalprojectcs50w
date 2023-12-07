from django import forms
from .models import Offer_job, User, User_profile, Application
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

# Create user account
class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if get_user_model().objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already in use.")
        return username
        

# User profile details (work experience, gradutation year, etc.)
class ProfileForm(forms.ModelForm):
    resume = forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={'accept': '.pdf'}))

    class Meta:
        model = User_profile
        exclude = ['user']


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User_profile
        fields = ['title', 'years', 'experience', 'habilities', 'resume']


# Available job places and companies
class JobForm(forms.ModelForm):
    class Meta:
        model = Offer_job
        fields = ['title', 'company_name', 'company_data', 'job_description', 'category', 'location', 'status']
        widgets = {
            'title': forms.Textarea(attrs={'cols': 80, 'rows': 3}),
            'company_name': forms.Textarea(attrs={'cols': 80, 'rows': 3}),
            'company_data': forms.Textarea(attrs={'cols': 80, 'rows': 3}),
            'job_description': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
            'category': forms.Textarea(attrs={'cols': 80, 'rows': 3}),
            'location': forms.Textarea(attrs={'cols': 80, 'rows': 3}),
        }


# Apply option
class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['job'] 
