from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    is_private = models.BooleanField()
    title = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='blog/images/%Y/%m/%d/', blank=True)
    content = models.TextField()
    category = models.ManyToManyField('Tag', blank=True)
    view_count = models.PositiveIntegerField(default=0)
    like_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'    
    
class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments'
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    like_count = models.PositiveIntegerField(default=0)
    message = models.TextField()

    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.message
    
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name