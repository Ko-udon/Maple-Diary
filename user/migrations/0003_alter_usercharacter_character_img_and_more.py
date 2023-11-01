# Generated by Django 4.2.6 on 2023-11-01 05:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0002_characterserver_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercharacter',
            name='character_img',
            field=models.ImageField(blank=True, upload_to='UserCharacter/images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='usercharacter',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
