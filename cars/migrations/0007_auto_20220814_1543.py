# Generated by Django 3.2.15 on 2022-08-14 15:43

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0006_alter_car_make'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='picture',
            new_name='photo_main',
        ),
        migrations.AddField(
            model_name='car',
            name='body_type',
            field=models.CharField(choices=[('Coupe', 'Coupe'), ('Saloon', 'Saloon'), ('Hatchback', 'Hatchback'), ('Estate', 'Estate'), ('SUV', 'SUV')], default='Coupe', max_length=50),
        ),
        migrations.AddField(
            model_name='car',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='car',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='car',
            name='engine_size',
            field=models.CharField(choices=[('1.0L', '1.0L'), ('1.1L', '1.1L'), ('1.2L', '1.2L'), ('1.3L', '1.3L'), ('1.4L', '1.4L'), ('1.5L', '1.5L'), ('1.6L', '1.6L'), ('1.7L', '1.7L'), ('1.8L', '1.8L'), ('1.9L', '1.9L'), ('2.0L', '2.0L'), ('2.5L', '2.5L'), ('3.0L', '3.0L'), ('3.5L', '3.5L'), ('4.0L', '4.0L'), ('5.0L', '5.0L')], default='1.0L', max_length=20),
        ),
        migrations.AddField(
            model_name='car',
            name='fuel_type',
            field=models.CharField(choices=[('Petrol', 'Petrol'), ('Diesel', 'Diesel'), ('Hybrid', 'Hybrid'), ('Electric', 'Electric')], default='Petrol', max_length=50),
        ),
        migrations.AddField(
            model_name='car',
            name='milage',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='car',
            name='photo_1',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='car',
            name='photo_2',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='car',
            name='photo_3',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='car',
            name='photo_4',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='car',
            name='photo_5',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, verbose_name='image'),
        ),
        migrations.AddField(
            model_name='car',
            name='price',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='car',
            name='transmission',
            field=models.CharField(choices=[('Manual', 'Manual'), ('Automatic', 'Automatic')], default='Manual', max_length=50),
        ),
        migrations.AddField(
            model_name='car',
            name='year',
            field=models.IntegerField(choices=[(2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022)], default=2022, verbose_name='year'),
        ),
        migrations.AlterField(
            model_name='car',
            name='make',
            field=models.CharField(choices=[('Audi', 'Audi'), ('Bmw', 'Bmw'), ('Citroen', 'Citroen'), ('Ford', 'Ford'), ('Mazda', 'Mazda'), ('Skoda', 'Skoda'), ('Toyota', 'Toyota'), ('Opel', 'Opel'), ('Lexus', 'Lexus'), ('Mercedes', 'Mercedes'), ('Volkswagen', 'Volksvagen'), ('Volvo', 'Volvo')], default='Audi', max_length=50),
        ),
    ]
