from django import forms
from catalog.models import Product, Version
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


class ProductForm(forms.ModelForm):
    version = forms.ModelChoiceField(queryset=Version.objects.all(), empty_label=None, label='Версия продукта')

    class Meta:
        model = Product
        fields = '__all__'

    BAN_LIST = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_banned_words(self, data):
        for item in self.BAN_LIST:
            if item in data.lower():
                raise forms.ValidationError('Ошибка! Вы используете запрещенные слова.')

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        self.clean_banned_words(cleaned_data)
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        self.clean_banned_words(cleaned_data)
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)

        # Получаем выбранную версию из данных формы
        selected_version = self.cleaned_data.get('version')

        # Связываем продукт с выбранной версией
        instance.version = selected_version

        if commit:
            instance.save()

        return instance
