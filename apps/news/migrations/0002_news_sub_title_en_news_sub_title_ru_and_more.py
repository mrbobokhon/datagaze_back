# Generated by Django 4.1.3 on 2022-12-01 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='sub_title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='sub title'),
        ),
        migrations.AddField(
            model_name='news',
            name='sub_title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='sub title'),
        ),
        migrations.AddField(
            model_name='news',
            name='sub_title_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='sub title'),
        ),
        migrations.AddField(
            model_name='news',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='news',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='title'),
        ),
        migrations.AddField(
            model_name='news',
            name='title_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='title'),
        ),
    ]
