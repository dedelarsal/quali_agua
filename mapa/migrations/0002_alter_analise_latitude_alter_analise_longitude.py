# Generated by Django 5.0.4 on 2024-04-18 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analise',
            name='latitude',
            field=models.DecimalField(decimal_places=15, max_digits=20),
        ),
        migrations.AlterField(
            model_name='analise',
            name='longitude',
            field=models.DecimalField(decimal_places=15, max_digits=20),
        ),
    ]