# posts/forms.py

from django import forms
from .models import Post, Photo

class PostForm(forms.ModelForm) :

    class Meta :
        model = Post
        fields = ['title', 'text', 'image1', 'image2', 'image3', 'image4', 'image5', 'gender', 'category']


class PhotoForm(forms.ModelForm) :

    class Meta :
        model = Photo
        fields = ['title', 'text', 'image1', 'image2', 'image3', 'image4', 'image5', 'gender', 'category']