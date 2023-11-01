from django import forms
from .models import UserCharacter

class UserCharacterForm(forms.ModelForm):
  class Meta:
    model = UserCharacter
    fields = ['character_name','character_server', 'character_img', 'profile_word']


