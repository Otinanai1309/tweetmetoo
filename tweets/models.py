from tkinter import CASCADE
from django.db import models
from django.conf import settings
import random


from platformdirs import user_cache_dir

User = settings.AUTH_USER_MODEL     # refferencies a build in django future for User model

# Create your models here.
class TweetLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey("Tweet", on_delete=models.CASCADE)   # i use quotes because Tweet model is below my TweetLike class
    timestamp = models.DateTimeField(auto_now_add=True)
    
class Tweet(models.Model):
    parent = models.ForeignKey("self", null=True, on_delete=models.SET_NULL) # "self" refers to the same instance of the Tweet
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # one user can have many tweets
    likes = models.ManyToManyField(User, related_name='tweet_user', blank=True, through=TweetLike)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.id}    {self.content}"
    class Meta:
        ordering = ['-id']  # descending order of new tweets
        
    @property
    def is_retweet(self):
        return self.parent != None
    
    
    def serialize(self):
        """
        Feel free to delete! Old way to serialize
        """
        return {
            "id": self.id,
            "content": self.content,
            "likes": random.randint(0, 1500), 
        } 
        
