# Generated by Django 3.2.5 on 2021-08-03 06:59

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lctl', '0020_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freelancer',
            name='freelancer_photo',
            field=models.ImageField(default='', storage=django.core.files.storage.FileSystemStorage(location='/media/Lctl/images'), upload_to=''),
        ),
        migrations.AlterField(
            model_name='img',
            name='photo',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/media/Lctl/images'), upload_to=''),
        ),
    ]
