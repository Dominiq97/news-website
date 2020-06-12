# Generated by Django 3.0.7 on 2020-06-10 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.TextField()),
                ('body', models.TextField()),
                ('name', models.CharField(max_length=12)),
                ('pic', models.TextField()),
                ('writer', models.CharField(max_length=50)),
            ],
        ),
    ]