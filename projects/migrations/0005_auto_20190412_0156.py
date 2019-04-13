# Generated by Django 2.1.7 on 2019-04-12 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20190412_0154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='blurb',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='cover',
            field=models.FilePathField(blank=True, default='', null=True, path='/img'),
        ),
        migrations.AlterField(
            model_name='project',
            name='demo',
            field=models.FilePathField(blank=True, default='', null=True, path='/img'),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='links',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='technology',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]