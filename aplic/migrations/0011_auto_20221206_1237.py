# Generated by Django 2.2.19 on 2022-12-06 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0010_auto_20221206_1135'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='codcliente',
        ),
        migrations.AddField(
            model_name='contrato',
            name='numero',
            field=models.CharField(default=1, max_length=10, verbose_name='Numero do Contrato'),
            preserve_default=False,
        ),
    ]
