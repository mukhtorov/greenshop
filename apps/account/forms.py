from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class LoginForm(forms.Form):
    username = forms.CharField(label='Enter your username and password to login.',
                               widget=forms.TextInput(
                                   attrs={'placeholder': 'almamun_uxui@outlook.com'}
                               ))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}), label='')


class NewUserForm(UserCreationForm):
    username = forms.CharField(label='', help_text='', widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(label='Enter your email and password to register.',
                             widget=forms.EmailInput(
                                 attrs={'placeholder': 'Enter your email address'}
                             ), required=True)
    password1 = forms.CharField(
        label=_(""),
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password',
                'placeholder': 'Password'
            }),
    )
    password2 = forms.CharField(
        label=_(''),
        widget=forms.PasswordInput(
            attrs={
                'autocomplete': 'new-password',
                'placeholder': 'Confirm Password'
            }),
        help_text=_(''),
    )

    class Meta:
        model = User
        fields = ('email',)

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

