# Generated by Django 5.1 on 2024-08-22 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_author_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
