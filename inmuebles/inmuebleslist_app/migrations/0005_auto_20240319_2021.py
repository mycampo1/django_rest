# Generated by Django 3.2.8 on 2024-03-19 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inmuebleslist_app', '0004_comentario_comentario_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='edificacion',
            name='avg_calificacion',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='edificacion',
            name='number_calificacion',
            field=models.IntegerField(default=0),
        ),
    ]
