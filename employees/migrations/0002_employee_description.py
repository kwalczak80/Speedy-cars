# Generated by Django 3.2.15 on 2022-08-13 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
