# Generated by Django 3.1.3 on 2020-11-15 01:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20201115_0343'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='image',
            new_name='fotoğraf',
        ),
    ]