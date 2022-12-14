# Generated by Django 2.2.19 on 2022-12-02 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplic', '0004_curso_imagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codcliente', models.CharField(max_length=10, verbose_name='Cadastro único do cliente')),
                ('cnpj', models.CharField(help_text='Formato XXX.XXX.XXX-XX', max_length=14, verbose_name='CNPJ')),
                ('razaosocial', models.CharField(max_length=50, verbose_name='Razão social')),
                ('gerente', models.CharField(max_length=50, verbose_name='Pessoa responsável')),
                ('email', models.EmailField(blank=True, max_length=200, verbose_name='E-mail da empresa')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Reuniao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datar', models.DateField(blank=True, help_text='Formato DD/MM/AAAA', null=True, verbose_name='Data da reunião')),
                ('hora', models.CharField(help_text='9h - 17h', max_length=2, verbose_name='Horário')),
                ('email', models.EmailField(blank=True, max_length=200, verbose_name='E-mail do invite')),
            ],
            options={
                'verbose_name': 'Reunião',
                'verbose_name_plural': 'Reuniões',
            },
        ),
    ]
