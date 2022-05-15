from dataclasses import fields
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django import forms
from django.conf import settings

from .models import Tweet

MAX_TWEET_LENGTH = settings.MAX_TWEET_LENGTH

class TweetForm(forms.ModelForm):
    
    # declare actual form
    class Meta:
        model = Tweet
        fields = ['content']
        
    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) > MAX_TWEET_LENGTH:
            raise forms.ValidationError("Thiw tweet is too long")
        return content
    
