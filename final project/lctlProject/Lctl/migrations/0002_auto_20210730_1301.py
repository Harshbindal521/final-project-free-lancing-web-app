# Generated by Django 3.2.5 on 2021-07-30 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lctl', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='freelancer',
            name='Country',
            field=models.CharField(default='India', max_length=30),
        ),
        migrations.AddField(
            model_name='freelancer',
            name='Phn',
            field=models.CharField(default='9999999999', max_length=15),
        ),
        migrations.AddField(
            model_name='freelancer',
            name='is_freelancer',
            field=models.BooleanField(default=False),
        ),
    ]
