# Generated by Django 3.2.15 on 2022-08-24 09:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20220823_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='date',
            field=models.DateField(default=datetime.date(2022, 8, 24)),
        ),
    ]
