# Generated by Django 4.2.4 on 2023-11-11 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0019_alter_archivo_archivo_oportunidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='oportunidad',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='oportunidades/'),
        ),
    ]
