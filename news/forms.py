from markdownx.fields import MarkdownxFormField
from django import forms

class ForumThreadForm(forms.Form):
    body = MarkdownxFormField()