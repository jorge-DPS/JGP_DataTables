# Generated by Django 3.0 on 2023-01-15 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cajas', '0003_auto_20221207_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallearqueo',
            name='creado_en',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
