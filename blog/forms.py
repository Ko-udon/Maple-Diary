from django import forms
from .models import Post, Comment, Tag

class PostForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ['is_private','title', 'image', 'content', 'category']


class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['message']

class TagForm(forms.ModelForm):
  class Meta:
    model = Tag
    fields = ['name']

