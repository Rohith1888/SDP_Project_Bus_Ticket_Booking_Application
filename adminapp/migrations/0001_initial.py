# Generated by Django 4.0.3 on 2024-03-09 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_type', models.CharField(choices=[('AC', 'AC'), ('NON-AC', 'Non-AC')], max_length=10)),
                ('bus_name', models.CharField(max_length=100)),
                ('bus_number', models.CharField(max_length=20, unique=True)),
                ('max_capacity', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BusRoute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_name', models.CharField(max_length=100)),
                ('source', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('timings', models.TimeField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
