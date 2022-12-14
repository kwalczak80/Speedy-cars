# Generated by Django 3.2.15 on 2022-08-13 14:47

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(choices=[('Audi', 'Audi'), ('Bmw', 'Bmw'), ('Ford', 'Ford'), ('Mazda', 'Mazda'), ('Toyota', 'Toyota'), ('Lexus', 'Lexus')], max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('fuel_type', models.CharField(choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('Hybrid', 'Hybrid'), ('Electric', 'Electric')], max_length=50)),
                ('year', models.IntegerField(choices=[(2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022)], default=2022, verbose_name='year')),
                ('body', models.CharField(choices=[('Saloon', 'Saloon'), ('Hatchback', 'Hatchback'), ('Coupe', 'Coupe'), ('Estate', 'Estate')], max_length=50)),
                ('transmmission', models.CharField(choices=[('Manual', 'Manual'), ('Automatic', 'Automatic')], max_length=50)),
                ('description', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('picture', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
            ],
        ),
    ]
