from django import forms
from captcha.fields import CaptchaField


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя',
                           max_length=100,
                           widget=forms.TextInput(attrs={'class': 'form-control', 'cols': 40, 'rows': 1}))
    email = forms.EmailField(label='E-mail',
                             widget=forms.TextInput(attrs={'class': 'form-control', 'cols': 40, 'rows': 1}))
    message = forms.CharField(label='Сообщение',
                              widget=forms.Textarea(attrs={'class': 'form-control', 'cols': 40, 'rows': 9}))
    captcha = CaptchaField(label='')


