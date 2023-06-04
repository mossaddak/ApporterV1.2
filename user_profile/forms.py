from django import forms
from .models import User

#user registration
class UserRegistrations(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password",)


    def clean_username(self):
        username = self.cleaned_data.get('username')
        model = self.Meta.model

        user = model.objects.filter(username__iexact=username)
        
        if user.exists():
            raise forms.ValidationError(
                "Ther User already exist with the given username")
        return self.cleaned_data.get('username')


    def clean_email(self):
        email = self.cleaned_data.get('email')
        model = self.Meta.model
        user = model.objects.filter(email__iexact=email)
        if user.exists():
            raise forms.ValidationError(
                "The email already exist with the given email")
        return self.cleaned_data.get('email')


    def clean_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Password do not match!")
        return self.cleaned_data.get('password')
    



class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)