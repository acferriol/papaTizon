# Generated by Django 4.1.2 on 2022-10-30 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estacion', '0001_initial'),
        ('clima', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clima',
            name='estacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='estacion.estacion'),
        ),
    ]
