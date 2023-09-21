# Generated by Django 4.2.4 on 2023-09-21 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre y Apellido')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo electrónico')),
                ('message', models.TextField(verbose_name='Mensaje')),
                ('contact_type', models.IntegerField(choices=[[0, 'Pedido de información'], [1, 'Queja por un producto'], [2, 'Felicitaciones'], [3, 'Otras']], verbose_name='Paises')),
                ('subscription', models.BooleanField(default=False, verbose_name='Suscribirme a correos informativos')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de envío')),
            ],
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre y Apellido')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo electrónico')),
                ('password', models.CharField(max_length=100, verbose_name='Password')),
                ('region', models.IntegerField(choices=[[0, 'Bogota-Colombia'], [1, 'Medellin-Colombia'], [2, 'Cali-Colombia'], [3, 'Otras']], verbose_name='Ciudad')),
                ('area', models.IntegerField(choices=[[0, 'Matematicas'], [1, 'Artes'], [2, 'Carpintero'], [3, 'Otras']], verbose_name='Area')),
                ('subscription', models.BooleanField(default=False, verbose_name='Suscribirme a correos informativos')),
            ],
        ),
        migrations.DeleteModel(
            name='Comentario',
        ),
    ]
