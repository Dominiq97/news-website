from markdownx.fields import MarkdownxFormField

class Body(forms.Form):
    body = MarkdownxFormField()