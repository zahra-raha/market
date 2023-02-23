from .models import Customer, Post
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'featured_image', 'category', 'color',
                  'dimensions', 'cost', 'address', 'condition', 'description')


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'phone', 'message')
