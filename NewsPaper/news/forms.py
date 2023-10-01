from django import forms
from django.core.exceptions import ValidationError
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'text',
            'postCategory',
            'author',
        ]

    labels = {
        'title': 'Title',
        'text': 'Text',
        'postCategory': 'Category',
        'author': 'Author',
    }

    def clean(self):
        cleaned_data = super().clean()
        text = cleaned_data.get('text')
        title = cleaned_data.get('title')

        if title == text:
            raise ValidationError(
                "Заголовок не должен совпадать с тексом."
            )

        return cleaned_data

    def clean_name(self):
        name = self.cleaned_data['name']

        if name[0].islower():
            raise ValidationError(
                "Название должно начинаться с заглавой буквы."
            )

        return name
