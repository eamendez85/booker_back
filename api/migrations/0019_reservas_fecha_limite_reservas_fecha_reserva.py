# Generated by Django 4.0.3 on 2022-06-01 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_alter_libros_imagen_libro'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservas',
            name='fecha_limite',
            field=models.DateTimeField(default="0001-01-01 01:01:01"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservas',
            name='fecha_reserva',
            field=models.DateTimeField(default="0001-01-01 01:01:01"),
            preserve_default=False,
        ),
    ]
