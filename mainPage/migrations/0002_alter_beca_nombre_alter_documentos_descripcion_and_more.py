# Generated by Django 4.2.5 on 2023-09-29 02:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainPage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beca',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='documentos',
            name='Descripcion',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='requisitos',
            name='Descripcion',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='universidad',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.CreateModel(
            name='Universidad_fav',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('Universidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainPage.universidad')),
            ],
        ),
    ]
