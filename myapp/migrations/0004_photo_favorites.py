# Generated by Django 5.2 on 2025-05-16 10:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_photo_is_pulic'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='favorites',
            field=models.ManyToManyField(blank=True, related_name='favorite_photos', to=settings.AUTH_USER_MODEL),
        ),
    ]
