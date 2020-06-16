from django import forms

from martor.fields import MartorFormField
from .models import News


class SimpleForm(forms.Form):
    title = forms.CharField(widget=forms.TextInput())
    description = MartorFormField()
    wiki = MartorFormField()


class PostForm(forms.ModelForm):

    class Meta:
        model = News
        fields = '__all__'