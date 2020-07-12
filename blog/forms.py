from django import forms
from .models import MyBlog

class BlogForm(forms.ModelForm):
    class Meta:
        model = MyBlog
        fields = '__all__'
        
