# Generated by Django 4.0.3 on 2022-05-06 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registromascota',
            old_name='adoptante',
            new_name='Apellidoadoptante',
        ),
        migrations.AddField(
            model_name='registromascota',
            name='Nombreadoptante',
            field=models.CharField(default='Disponible', max_length=50),
        ),
    ]
