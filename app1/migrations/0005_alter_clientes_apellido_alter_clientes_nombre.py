# Generated by Django 4.2.7 on 2023-11-06 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_rename_comision_clientes_apellido'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='Apellido',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='nombre',
            field=models.CharField(max_length=12),
        ),
    ]