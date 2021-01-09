from django import forms
from .models import Article

class addArticle(forms.ModelForm):
    class Meta:
        model=Article
        fields=["title","content","article_img"]