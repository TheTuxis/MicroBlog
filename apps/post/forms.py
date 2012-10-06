# -*- coding: utf-8 *-*
from django.forms import ModelForm

from apps.post.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['author', ]
