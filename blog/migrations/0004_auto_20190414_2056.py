# Generated by Django 2.1.7 on 2019-04-14 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_blurb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='blurb',
            field=models.CharField(blank=True, default='', max_length=250, null=True),
        ),
    ]