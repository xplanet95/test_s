import re
from django import forms
from .models import News, Category
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import User
from captcha.fields import CaptchaField


# сохранять данные не будем
class ContactUsForm(forms.Form):
    subject = forms.CharField(label='Тема', widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    # 'style': 'width: 25%',
    }))
    email = forms.EmailField(label='e-mail получателя', widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    # 'style': 'width: 25%',
    }))
    body = forms.CharField(label='Текст', widget=forms.Textarea(attrs={
        'class': 'form-control',
        'rows': 5,
        # 'style': 'width: 25%',
    }))
    captcha = CaptchaField()


# AuthenticationForm делает за нас аутентификацию, в нем нет Meta
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Логин:', widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'style': 'width: 25%',
    }))
    password = forms.CharField(label='Пароль:', widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'style': 'width: 25%'}))


class UserRegisterForm(UserCreationForm):
    # убрать автофокус
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.pop('autofocus')

    username = forms.CharField(label='Логин:', help_text='Только давай нормальный логин',
                               widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'style': 'width: 25%',
    }))
    email = forms.EmailField(label='e-mail:', widget=forms.EmailInput(attrs={'class': 'form-control',
                                          'style': 'width: 25%'}))
    password1 = forms.CharField(label='Пароль:', widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'style': 'width: 25%'}))
    password2 = forms.CharField(label='Подтвердите пароль:', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'style': 'width: 25%'
    }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class NewsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(NewsForm, self).__init__(*args, **kwargs)

        self.fields['category'].empty_label = 'Выберите категорию'
        self.fields['content'].label = 'Текст новости'

    class Meta:
        model = News
        # fields = '__all__'
        fields = ['title', 'content', 'is_published', 'category', 'photo']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={
                                          'class': 'form-control',
                                          'style': 'width: 25%'
                                      }),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('В начале не может быть цифры')
        return title

#  форма не связанная с моделью (связь прописываем сами)
# class NewsForm(forms.Form):
#     title = forms.CharField(max_length=150,
#                             label='Заголовок:',
#                             widget=forms.TextInput(attrs={'class': 'form-control'}))
#     content = forms.CharField(label='Текст новости:',
#                               required=False,
#                               widget=forms.Textarea(attrs={'class': 'form-control'}))
#     is_published = forms.BooleanField(label='Опубликовать (да/нет):',
#                                       initial=True)
#     category = forms.ModelChoiceField(queryset=Category.objects.all(),
#                                       label='Категория:',
#                                       empty_label='Выберите категорию:',
#                                       widget=forms.Select(attrs={
#                                           'class': 'form-control',
#                                           'style': 'width: 25%'
#                                       }))
