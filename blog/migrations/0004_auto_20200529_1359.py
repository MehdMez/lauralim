# Generated by Django 2.2.12 on 2020-05-29 11:59

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200529_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recette',
            name='ingredients',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(default=''), size=None), size=None),
        ),
        migrations.AlterField(
            model_name='recette',
            name='preparation',
            field=django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(default=''), size=None), size=None),
        ),
    ]
