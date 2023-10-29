# Generated by Django 3.2.5 on 2021-07-31 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lctl', '0006_freelancer_payperhr'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_username', models.CharField(max_length=25)),
                ('freelancer_username', models.CharField(max_length=25)),
                ('work_desc', models.CharField(max_length=500)),
                ('order_amount', models.CharField(max_length=10)),
            ],
        ),
    ]
