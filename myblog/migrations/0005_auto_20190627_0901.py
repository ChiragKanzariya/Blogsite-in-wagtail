# Generated by Django 2.2 on 2019-06-27 09:01

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('myblog', '0004_auto_20190627_0843'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'verbose_name_plural': 'blog categories',
            },
        ),
        migrations.AddField(
            model_name='blogpage',
            name='blog_categories',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='myblog.BlogCategory'),
        ),
    ]