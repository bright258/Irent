# Generated by Django 4.0 on 2022-08-05 15:43

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_rename_video1_house_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='house',
            name='video',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True),
        ),
    ]
