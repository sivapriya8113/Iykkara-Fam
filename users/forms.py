from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254,required=True)
    birth_date = forms.DateField(help_text='Required.Format: YYYY-MM-DD')
    Gender = forms.CharField(required=True,widget=forms.Select(choices=([('male', 'Male'),('female','Female'),('na', 'NA')])))
    profile_image = forms.FileField(required=True)


    class Meta:
        model = User
        fields = ('first_name', 'last_name','username','email','profile_image','birth_date','Gender','password1', 'password2', )
