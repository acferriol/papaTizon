# Generated by Django 4.1.2 on 2022-11-11 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clima', '0005_alter_clima_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clima',
            name='fecha',
            field=models.DateField(default='2022-11-11'),
        ),
        migrations.AlterField(
            model_name='clima',
            name='temperatura_media',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True),
        ),
    ]
