# Generated by Django 3.0.1 on 2020-02-10 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20200210_0606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='phone',
            field=models.CharField(default='00000', max_length=30),
        ),
        migrations.AlterField(
            model_name='account',
            name='role',
            field=models.CharField(default='Manager', max_length=15),
        ),
    ]
