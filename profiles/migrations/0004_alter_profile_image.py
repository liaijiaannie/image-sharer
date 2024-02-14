# Generated by Django 5.0.2 on 2024-02-12 23:32

import sorl.thumbnail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=sorl.thumbnail.fields.ImageField(default='/media/profiles/default.jpeg', upload_to='profiles'),
        ),
    ]