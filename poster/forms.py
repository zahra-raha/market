from .models import Category, Post
from django import forms


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'color', 'dimensions',)