# Generated by Django 3.2.15 on 2022-09-08 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0010_alter_car_sales_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='body_type',
            field=models.CharField(choices=[('Coupe', 'Coupe'), ('Cabriolet', 'Cabriolet'), ('Saloon', 'Saloon'), ('Hatchback', 'Hatchback'), ('Estate', 'Estate'), ('SUV', 'SUV')], default='Coupe', max_length=50),
        ),
    ]
