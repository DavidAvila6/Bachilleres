# Generated by Django 4.2.5 on 2023-11-16 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0030_remove_usuariooportunidad_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuariooportunidad',
            name='nuevo_campo',
        ),
    ]
