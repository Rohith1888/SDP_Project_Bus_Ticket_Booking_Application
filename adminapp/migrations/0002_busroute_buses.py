# Generated by Django 4.0.3 on 2024-03-09 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='busroute',
            name='buses',
            field=models.ManyToManyField(to='adminapp.bus'),
        ),
    ]