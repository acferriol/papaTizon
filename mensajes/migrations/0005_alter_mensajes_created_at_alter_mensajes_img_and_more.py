# Generated by Django 4.1.2 on 2022-11-27 03:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mensajes', '0004_alter_mensajes_created_at_alter_mensajes_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mensajes',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 26, 22, 13, 15, 786539)),
        ),
        migrations.AlterField(
            model_name='mensajes',
            name='img',
            field=models.FileField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='mensajes',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 26, 22, 13, 15, 786539)),
        ),
    ]
