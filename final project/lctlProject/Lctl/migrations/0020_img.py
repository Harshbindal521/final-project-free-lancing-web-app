# Generated by Django 3.2.5 on 2021-08-03 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lctl', '0019_alter_freelancer_freelancer_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='Lctl/images')),
            ],
        ),
    ]
