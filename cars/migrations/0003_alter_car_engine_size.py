# Generated by Django 3.2.15 on 2022-08-13 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20220813_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='engine_size',
            field=models.FloatField(),
        ),
    ]
