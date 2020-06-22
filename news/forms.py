from django import forms
from martor.fields import MartorFormField
from news.models import News


class SimpleForm(forms.Form):
    description = MartorFormField()


class PostForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'
