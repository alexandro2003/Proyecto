# Generated by Django 4.2.4 on 2023-08-10 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('dni', models.CharField(max_length=8)),
                ('correoelectronico', models.CharField(max_length=50)),
                ('contraseña', models.CharField(max_length=20)),
            ],
        ),
    ]
