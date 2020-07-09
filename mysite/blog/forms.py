from django.core import validators

from .models import Comment, Post
from django import forms


class PostForm(forms.ModelForm):
    botcatcher = forms.CharField(widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    class Meta:
        model = Post
        fields = ('author', 'title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'})
            }


class CommentForm(forms.ModelForm):
    botcatcher = forms.CharField(widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    class Meta:
        model = Comment
        fields = ('author', 'text')
        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})
            }
