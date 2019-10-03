from django import forms
from .models import blog_post


class PublishForm(forms.ModelForm):
    class Meta:
        model = blog_post
        fields = {'post_text', 'post_image', }