from django.core import validators

from .models import Comment, Post
from django import forms


class PostForm(forms.ModelForm):
    botcatcher = forms.CharField(widget=forms.HiddenInput, required=False,
                                 validators=[validators.MaxLengthValidator(0)])

    class Meta:
        model = Post
        fields = ('author', 'title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'titleinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea textinputclass',
                                          'placeholder': 'Write your text here'})}


class CommentForm(forms.ModelForm):
    botcatcher = forms.CharField(widget=forms.HiddenInput, required=False,
                                 validators=[validators.MaxLengthValidator(0)])
    author = forms.CharField(validators=[validators.MaxLengthValidator(15)])


    author.widget.attrs.update({'class': 'textinputclass',
                                'placeholder': 'Your name (max 15 characters)'})

    class Meta:
        model = Comment
        fields = ('author', 'text')
        widgets = {
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea textinputclass',
                                          'placeholder': 'Your comment'})
            }
