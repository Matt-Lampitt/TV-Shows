# Generated by Django 2.2 on 2021-02-20 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tv_shows', '0002_show_desciription'),
    ]

    operations = [
        migrations.RenameField(
            model_name='show',
            old_name='desciription',
            new_name='description',
        ),
    ]
