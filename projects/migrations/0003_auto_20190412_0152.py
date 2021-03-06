# Generated by Django 2.1.7 on 2019-04-12 01:52

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20190412_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='links',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(default=''), default=list, size=None),
        ),
        migrations.AlterField(
            model_name='project',
            name='technology',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default='', max_length=50), default=list, size=None),
        ),
    ]
