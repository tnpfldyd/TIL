from django import forms
from .models import Article
from django.core.exceptions import ValidationError

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
    def clean_title(self):
        title = self.cleaned_data['title']
        if '*' in title:
            raise ValidationError('*은 제목에 들어갈 수 없습니다.')
        return title