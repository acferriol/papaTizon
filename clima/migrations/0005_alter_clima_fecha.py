# Generated by Django 4.1.2 on 2022-11-09 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clima', '0004_alter_clima_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clima',
            name='fecha',
            field=models.DateField(default='2022-11-09'),
        ),
    ]
