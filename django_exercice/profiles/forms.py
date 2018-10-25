from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password', 'placeholder': 'Password'}))
                            


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username', 'placeholder': 'Username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'first_name', 'placeholder': 'Firstname'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'last_name', 'placeholder': 'Lastname'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'name': 'email', 'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password1', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password2', 'placeholder': 'confirm your password'}))

class EditProfileForm(UserChangeForm):

    class Meta:
         model = User
         fields = ('email','password')
         excludes = ('password')
         email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'name': 'email'}))

   