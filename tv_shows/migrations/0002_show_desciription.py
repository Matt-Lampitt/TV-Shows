# Generated by Django 2.2 on 2021-02-20 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_shows', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='desciription',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
