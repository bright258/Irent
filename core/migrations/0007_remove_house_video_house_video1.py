# Generated by Django 4.0 on 2022-08-05 10:58

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_house_image1_house_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='video',
        ),
        migrations.AddField(
            model_name='house',
            name='video1',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='video'),
        ),
    ]
