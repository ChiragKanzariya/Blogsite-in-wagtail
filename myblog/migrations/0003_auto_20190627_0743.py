# Generated by Django 2.2 on 2019-06-27 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0002_auto_20190627_0723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='blog_content',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]