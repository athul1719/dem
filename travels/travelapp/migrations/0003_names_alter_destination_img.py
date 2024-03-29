# Generated by Django 4.2.7 on 2023-11-30 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_rename_place_destination'),
    ]

    operations = [
        migrations.CreateModel(
            name='names',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='pics')),
                ('desc', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='destination',
            name='img',
            field=models.ImageField(upload_to='gallery'),
        ),
    ]
