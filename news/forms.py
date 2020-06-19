from django import forms

from martor.fields import MartorFormField
from .models import News


class SimpleForm(forms.Form):
    body = MartorFormField()


class PostForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'