# Generated by Django 2.2.12 on 2020-06-01 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200529_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='photo',
            field=models.ImageField(upload_to='uploads/category_img'),
        ),
    ]
