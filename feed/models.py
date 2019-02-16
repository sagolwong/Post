from django.db import models


class Post(models.Model):
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    text = models.TextField()
    
    def __str__(self):
        return self.title