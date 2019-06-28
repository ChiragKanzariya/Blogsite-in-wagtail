# Generated by Django 2.2 on 2019-06-28 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homepage',
            options={'verbose_name': 'Welcome Page', 'verbose_name_plural': 'Welcome Pages'},
        ),
        migrations.AddField(
            model_name='homepage',
            name='welcome_title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
