# Generated by Django 3.0.1 on 2020-02-10 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20200210_0607'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='account',
            name='role',
        ),
    ]