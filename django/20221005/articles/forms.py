from django.core.exceptions import ValidationError
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 5:
            raise ValidationError('제목은 5글자 이상이어야 합니다.')
        return title
    def clean_content(self):
        content = self.cleaned_data['content']
        if len(content) < 10:
            raise ValidationError('내용은 10글자 이상이어야 합니다.')
        return content