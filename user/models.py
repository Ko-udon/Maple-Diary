from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserCharacter(models.Model):
    
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_character'
    )
    character_name = models.TextField()
    character_server = models.TextField()
    character_img = models.ImageField(
        upload_to='tube/images/%Y/%m/%d/', blank=True)
    profile_word = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.message
