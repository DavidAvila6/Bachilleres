# Generated by Django 4.2.4 on 2023-10-03 01:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0010_merge_20231002_2014'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='becas_fav',
            name='unique_foraneas_favoritos_Beca',
        ),
        migrations.AddField(
            model_name='becas_fav',
            name='tipo',
            field=models.CharField(choices=[('facultad', 'facultad'), ('beca', 'beca')], default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddConstraint(
            model_name='becas_fav',
            constraint=models.UniqueConstraint(fields=('usuario', 'Configuracion_Becas', 'tipo'), name='unique_foraneas_favoritos_Beca'),
        ),
    ]
