# Generated by Django 4.0.4 on 2022-05-28 21:14

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='uploads'),
        ),
        migrations.AlterField(
            model_name='article',
            name='thumbnail',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='uploads'),
        ),
    ]
