# Generated by Django 3.0 on 2023-01-15 15:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Artist',
                'verbose_name_plural': 'Artists',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genres',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Name')),
                ('rank', models.PositiveIntegerField(verbose_name='Rank')),
                ('year', models.PositiveIntegerField(verbose_name='Year')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='albums.Artist', verbose_name='Artist')),
                ('genres', models.ManyToManyField(related_name='albums', to='albums.Genre', verbose_name='Genres')),
            ],
            options={
                'verbose_name': 'Album',
                'verbose_name_plural': 'Albums',
                'db_table': 'tabla_album',
                'ordering': ['name'],
            },
        ),
    ]
