from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class User(models.Model):
#     def save(self):
#         if is_new:
#             UserCharacter.objects.create(user=self)

#사용자 추가 프로필, 
class UserCharacter(models.Model):
    
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    # , related_name='user_character'
    character_name = models.TextField(blank=True, verbose_name="캐릭터 이름")
    character_server = models.ManyToManyField('CharacterServer', verbose_name="캐릭터 서버", blank=True) 
    character_img = models.ImageField(
        upload_to='UserCharacter/images/%Y/%m/%d/', verbose_name="캐릭터 이미지", blank=True)
    profile_word = models.TextField(verbose_name="자기소개", blank=True)
    maple_api_key = models.TextField(verbose_name="API 키", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.character_name

class CharacterServer(models.Model):
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name