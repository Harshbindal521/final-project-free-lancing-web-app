# Generated by Django 3.2.5 on 2021-07-31 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lctl', '0007_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freelancer',
            name='freelancer_photo',
            field=models.ImageField(default='/media/Lctl/images/default.png', upload_to='Lctl/images'),
        ),
    ]
