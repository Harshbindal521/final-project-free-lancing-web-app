# Generated by Django 3.2.5 on 2021-07-31 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lctl', '0009_freelancer_aboutdesc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freelancer',
            name='aboutdesc',
            field=models.CharField(default='', max_length=2000),
        ),
    ]