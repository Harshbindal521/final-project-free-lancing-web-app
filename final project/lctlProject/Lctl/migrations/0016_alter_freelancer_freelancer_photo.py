# Generated by Django 3.2.5 on 2021-08-02 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lctl', '0015_alter_freelancer_freelancer_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freelancer',
            name='freelancer_photo',
            field=models.ImageField(default='', upload_to='skillhub/images/'),
        ),
    ]
