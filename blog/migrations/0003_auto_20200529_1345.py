# Generated by Django 2.2.12 on 2020-05-29 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200529_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='recette',
            name='photo3',
            field=models.ImageField(blank=True, upload_to='uploads/% Y/% m/% d/'),
        ),
        migrations.AddField(
            model_name='recette',
            name='photo4',
            field=models.ImageField(blank=True, upload_to='uploads/% Y/% m/% d/'),
        ),
    ]