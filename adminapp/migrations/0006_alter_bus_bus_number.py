# Generated by Django 4.0.3 on 2024-03-09 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0005_remove_busroute_allocated_bus_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='bus_number',
            field=models.IntegerField(unique=True),
        ),
    ]
