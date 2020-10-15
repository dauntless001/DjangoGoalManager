from django import forms
from django.contrib.auth import get_user_model

class LoginForm(forms.Form):
    username = forms.CharField(max_length=20, 
    widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=20, 
    widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20, 
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    email = forms.EmailField( 
        widget=forms.EmailInput(attrs={'class': 'form-control'}))

    password = forms.CharField(max_length=20, 
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    confirm_password = forms.CharField(max_length=20, 
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    

    def clean(self):
        data = self.cleaned_data
        return self.data
    
    def get_username(self):
        User = get_user_model()
        username = self.cleaned_data.get('username')
        qs = User.objects.get(username=username)
        if qs:
            raise forms.ValidationError('Username Taken. Try Again')
        return username
    
    def get_password(self):
        password = self.cleaned_data.get('password')
        password_confirmed  = self.cleaned_data.get('confirm_password')


        if len(password) > 8:
            if password != password_confirmed:
                raise forms.ValidationError('Password must match')
        else:
            raise forms.ValidationError('Password must not be less than 8 characters')

        return password
    