from django.db import models
from django.conf import settings
import random

User = settings.AUTH_USER_MODEL     # refferencies a build in django future for User model

# Create your models here.
class Tweet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # one user can have many tweets
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    
    class Meta:
        ordering = ['-id']  # descending order of new tweets
        
    
    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "likes": random.randint(0, 1500), 
        } 