# Generated by Django 5.0.2 on 2024-02-12 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
