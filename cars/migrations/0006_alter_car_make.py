# Generated by Django 3.2.15 on 2022-08-13 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_auto_20220813_1648'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='make',
            field=models.CharField(choices=[('Audi', 'Audi'), ('Bmw', 'Bmw'), ('Citroen', 'Citroen'), ('Ford', 'Ford'), ('Mazda', 'Mazda'), ('Skoda', 'Skoda'), ('Toyota', 'Toyota'), ('Opel', 'Opel'), ('Lexus', 'Lexus'), ('Mercedes', 'Mercedes'), ('Volkswagen', 'Volksvagen'), ('Volvo', 'Volvo')], max_length=50),
        ),
    ]
