from django import forms

from .models  import Post
class PostForm(forms.ModelForm):
    class Meta: # This class tells that which model should be used to create this form.
        model=Post
        fields=('title','text',)

