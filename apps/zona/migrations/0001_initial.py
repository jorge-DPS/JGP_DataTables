# Generated by Django 3.0 on 2022-10-27 15:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresa', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Localidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50, verbose_name='Descripción Localidad')),
                ('codigo_departamento', models.CharField(max_length=2, verbose_name='codigo_departamento')),
                ('codigo_localidad', models.CharField(max_length=2, verbose_name='codigo_localidad')),
                ('creado_en', models.DateTimeField(auto_now_add=True)),
                ('actualizado_en', models.DateTimeField(auto_now=True, null=True)),
                ('eliminado_en', models.DateTimeField(blank=True, null=True, verbose_name='Fecha Eliminacion')),
                ('sucursal_creacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.Sucursal')),
                ('usuario_actualizacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Localidad',
                'verbose_name_plural': 'Localidades',
                'db_table': 'cli_tbl_localidad',
            },
        ),
        migrations.CreateModel(
            name='Zona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50, verbose_name='Descripcion de zona')),
                ('creado_en', models.DateTimeField()),
                ('actualizado_en', models.DateTimeField(blank=True, null=True)),
                ('eliminado_en', models.DateTimeField(blank=True, null=True, verbose_name='Fecha Eliminacion')),
                ('localidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zona.Localidad')),
                ('sucursal_creacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.Sucursal')),
                ('usuario_actualizacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Zona',
                'verbose_name_plural': 'Zonas',
                'db_table': 'cli_tbl_zona',
                'unique_together': {('descripcion', 'localidad')},
            },
        ),
    ]