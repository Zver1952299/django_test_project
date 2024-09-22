from .models import Article
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'anons', 'text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': "form-control"
            }),
            'anons': TextInput(attrs={
                'class': "form-control"
            }),
            'text': Textarea(attrs={
                'class': "form-control"
            }),
            'date': DateTimeInput(attrs={
                'class': "form-control"
            }),
        }
