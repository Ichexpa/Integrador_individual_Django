# Generated by Django 4.2.1 on 2023-05-16 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=50)),
                ('apellido', models.CharField(default='', max_length=50)),
                ('dni', models.CharField(default='Sin especificar', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='', max_length=50)),
                ('precio', models.FloatField(default=0)),
                ('stock_actual', models.IntegerField(default=0)),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proveedor', to='compra.proveedor')),
            ],
        ),
    ]