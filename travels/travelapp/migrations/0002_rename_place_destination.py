# Generated by Django 4.2.7 on 2023-11-25 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='place',
            new_name='destination',
        ),
    ]
