# Generated by Django 3.2.5 on 2021-08-02 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lctl', '0018_freelancer_freelancer_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freelancer',
            name='freelancer_photo',
            field=models.ImageField(default='', upload_to='Lctl/images'),
        ),
    ]