from django import forms

from app.models import Post


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['cover']
