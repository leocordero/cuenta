# Generated by Django 3.2.5 on 2021-07-30 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20210730_0131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario_fisico',
            name='connector',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='inventario_fisico',
            name='module_name',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='inventario_fisico',
            name='plugg_type',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='inventario_fisico',
            name='port',
            field=models.CharField(max_length=60),
        ),
    ]
