# Generated by Django 4.2.7 on 2023-11-06 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_alter_clientes_apellido_alter_clientes_nombre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientes',
            name='nombre',
        ),
        migrations.AlterField(
            model_name='clientes',
            name='Apellido',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='clientes',
            name='Nombre',
            field=models.CharField(default='', max_length=15),
        ),
    ]
