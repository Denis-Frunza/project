from django import forms


class UserCreationForm(forms.Form):
    customer_name = forms.CharField(max_length=40)
    email = forms.EmailField()
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
