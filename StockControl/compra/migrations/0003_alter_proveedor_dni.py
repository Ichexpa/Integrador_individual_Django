# Generated by Django 4.2.1 on 2023-05-17 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compra', '0002_alter_proveedor_dni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='dni',
            field=models.IntegerField(default=0),
        ),
    ]