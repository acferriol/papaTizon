# Generated by Django 4.1.2 on 2022-11-09 00:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0001_initial'),
        ('users', '0003_alter_user_empresa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.empresa'),
        ),
    ]
