# Generated by Django 5.1.1 on 2024-09-06 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='default_pfoto.png', upload_to='profile_images'),
        ),
    ]
