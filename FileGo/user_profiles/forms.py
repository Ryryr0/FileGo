from django import forms
from django.contrib.auth import get_user_model


class ProfileSettingsForm(forms.ModelForm):
    username = forms.CharField(label='Login', disabled=True, widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.CharField(label='E-mail', disabled=True, widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name']
        labels = {
            'first_name': 'First name',
            'last_name': 'Last name',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
        }
