from django import forms
from .models import ArticlePost

class ArticlePostFrom(forms.ModelForm):
    class Meta:
        model = ArticlePost
        fields = ('title', 'body')