# Generated by Django 4.1.2 on 2022-11-16 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0004_alter_aparicion_fecha_alter_datosplantacion_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aparicion',
            name='fecha',
            field=models.DateField(default='2022-11-15'),
        ),
        migrations.AlterField(
            model_name='datosplantacion',
            name='fecha',
            field=models.DateField(default='2022-11-15'),
        ),
    ]
