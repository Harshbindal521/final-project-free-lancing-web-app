# Generated by Django 3.2.5 on 2021-07-31 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lctl', '0010_alter_freelancer_aboutdesc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freelancer',
            name='desc',
            field=models.CharField(default=' ', max_length=250),
        ),
    ]