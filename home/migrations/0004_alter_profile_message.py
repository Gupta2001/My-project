# Generated by Django 4.0.4 on 2022-07-01 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='message',
            field=models.TextField(default='There is No messages from Vidya Ashram'),
        ),
    ]
