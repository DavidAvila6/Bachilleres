# Generated by Django 4.2.5 on 2023-10-16 18:15

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainPage', '0006_alter_elegirrespuesta_id_alter_pregunta_id_usuario_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Usuario',
            new_name='QuizUsuario',
        ),
    ]
