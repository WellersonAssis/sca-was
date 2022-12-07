# Generated by Django 2.2.19 on 2022-12-06 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0012_auto_20221206_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='contrato',
            name='nome',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='aplic.Servico'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contrato',
            name='razaosocial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='aplic.Cliente'),
        ),
        migrations.AlterField(
            model_name='relatoriofinal',
            name='razaosocial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='aplic.Cliente'),
        ),
        migrations.AlterField(
            model_name='reuniao',
            name='razaosocial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='aplic.Cliente'),
        ),
    ]
