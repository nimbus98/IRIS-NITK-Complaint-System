# Generated by Django 2.0.6 on 2018-07-13 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portalapp', '0015_auto_20180713_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='approval',
            field=models.IntegerField(default=0),
        ),
    ]
