# Generated by Django 4.0.4 on 2022-05-04 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0003_comment_datepy_added'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='datepy_added',
        ),
    ]
