# Generated by Django 5.1 on 2024-08-22 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(blank=True, default='', max_length=20000),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('1', 'Design'), ('2', 'Movies'), ('3', 'Travelling')], default='1', max_length=30),
        ),
    ]
