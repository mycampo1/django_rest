# Generated by Django 3.2.8 on 2024-03-19 17:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inmuebleslist_app', '0003_auto_20240319_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='comentario_user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
