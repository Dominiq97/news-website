# Generated by Django 3.0.7 on 2020-06-10 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20200610_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='fb',
            field=models.TextField(default='-', max_length=60),
        ),
        migrations.AlterField(
            model_name='main',
            name='link',
            field=models.TextField(default='-', max_length=60),
        ),
        migrations.AlterField(
            model_name='main',
            name='set_name',
            field=models.TextField(default='-', max_length=60),
        ),
        migrations.AlterField(
            model_name='main',
            name='tel',
            field=models.TextField(default='-', max_length=60),
        ),
        migrations.AlterField(
            model_name='main',
            name='tw',
            field=models.TextField(default='-', max_length=60),
        ),
        migrations.AlterField(
            model_name='main',
            name='yt',
            field=models.TextField(default='-', max_length=60),
        ),
    ]
