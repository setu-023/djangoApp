# Generated by Django 3.0.1 on 2020-02-16 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20200211_0506'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_check',
            field=models.BooleanField(default=True),
        ),
    ]
