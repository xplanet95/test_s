from django import forms
from .models import News, Category
import re
from django.core.exceptions import ValidationError


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
