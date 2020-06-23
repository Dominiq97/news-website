from django import forms

from martor.fields import MartorFormField
from .models import News


class SimpleForm(forms.Form):
    body = MartorFormField()


class PostForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        # Aici initializam form-ul cu some_body
        # primit din views.py news_edit
        body = kwargs.pop('some_body', None)
        super(PostForm, self).__init__(*args, **kwargs)
        if body:
            self.fields['body'].initial = body