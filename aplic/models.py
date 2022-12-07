from django.db import models
from django.db import models

# Create your models here.

from django.db import models
from stdimage.models import StdImageField

import uuid


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]

    filename = f'{uuid.uuid4()}.{ext}'

    return filename


class Funcionario(models.Model):

    codFunc = models.CharField('Código Funcionário', max_length=10)

    cpf = models.CharField('CPF', max_length=11)

    funcao = models.CharField('Função', max_length=20)

    nome = models.CharField('Nome', max_length= 40)

    class Meta:
        verbose_name = 'Funcionário'

        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return f"{self.nome} / {self.codFunc}"

class Cliente(models.Model):

    cnpj = models.CharField('CNPJ', max_length=18, help_text='Formato XX.XXX.XXX/XXXX-XX')

    razaosocial = models.CharField('Razão social', max_length=50)

    gerente = models.CharField('Pessoa responsável', max_length=50)

    email = models.EmailField('E-mail da empresa', blank=True, max_length=200)


    class Meta:
        verbose_name = 'Cliente'

        verbose_name_plural = 'Clientes'

    def __str__(self):
        return f"{self.razaosocial} / {self.cnpj}"


class Servico(models.Model):

    nivel = models.CharField('Nível',max_length=10)

    nome = models.CharField('Nome', max_length=20)

    valor = models.CharField('Valor', max_length=10)


    class Meta:
        verbose_name = 'Serviço'

        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.nome


class RelatoriodeRede(models.Model):

    razaosocial = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)

    descRede = models.TextField('Descrição de Rede', max_length=500)

    numDispositivos = models.IntegerField('Dispositivos')

    codFunc = models.ForeignKey(Funcionario, on_delete=models.DO_NOTHING)

    emailEmpresa = models.EmailField('Email Cliente', max_length=30)

    firewall = models.CharField('Firewall', max_length=20)

    antivirus = models.CharField('Antivírus', max_length=20)

    class Meta:
        verbose_name = 'Relatório de Rede'

        verbose_name_plural = 'Relatórios de Rede'

    def __str__(self):
        return f"{self.razaosocial} / {self.descRede}"



class Contrato(models.Model):

    codFunc = models.ForeignKey(Funcionario, on_delete=models.DO_NOTHING)

    razaosocial = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)

    numero = models.CharField('Numero do Contrato', max_length=10)

    nome = models.ForeignKey(Servico, on_delete=models.DO_NOTHING)



    class Meta:

        verbose_name = 'Contrato'

        verbose_name_plural = 'Contratos'

    def __str__(self):
        return self.numero


class RelatorioFinal(models.Model):

    codFunc = models.ForeignKey(Funcionario, on_delete=models.DO_NOTHING)

    razaosocial = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)

    emailEmpresa = models.EmailField('Email Cliente', max_length=30)

    descPentest = models.CharField('Descrição do Pentest', max_length=500)

    class Meta:
        verbose_name = 'Relatório Final'

        verbose_name_plural = 'Relatórios Finais'

    def __str__(self):
        return f"{self.cnpj} / {self.codFunc} / {self.descPentest}"


class Reuniao(models.Model):

    razaosocial = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)

    data = models.DateField('Data da reunião', blank=True, null=True, help_text='Formato DD/MM/AAAA')

    hora = models.CharField('Horário', max_length=2, help_text='9h - 17h')

    email = models.EmailField('E-mail do invite', blank=True, max_length=50)

    codFunc = models.ForeignKey(Funcionario, on_delete=models.DO_NOTHING)


    class Meta:
        verbose_name = 'Reunião'

        verbose_name_plural = 'Reuniões'

        def __str__(self):
            return f"{self.data} / {self.hora}"