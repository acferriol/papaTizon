# Generated by Django 4.1.2 on 2022-11-09 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clima', '0003_clima_empresa_alter_clima_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clima',
            name='fecha',
            field=models.DateField(default='2022-11-08'),
        ),
    ]