# Generated by Django 4.2.7 on 2023-11-06 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_clientes_rename_curso_fondos_inversion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='acciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('ticket', models.CharField(max_length=6)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='bonos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('ticket', models.CharField(max_length=6)),
                ('valor_nominal', models.IntegerField()),
                ('valor_mercado', models.IntegerField()),
                ('tir', models.IntegerField()),
            ],
        ),
    ]
