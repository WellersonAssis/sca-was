from django.contrib import admin

from .models import Cliente, Funcionario, Reuniao, Servico, RelatoriodeRede, Contrato, RelatorioFinal


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'funcao', 'codFunc', 'nome' )


@admin.register(RelatoriodeRede)
class RelatoriodeRedeAdmin(admin.ModelAdmin):
    list_display = ('razaosocial','emailEmpresa', 'codFunc', 'numDispositivos', 'antivirus', 'firewall', 'descRede')


@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nivel', 'nome', 'valor')


@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = ('codFunc', 'razaosocial', 'numero','nome')


@admin.register(RelatorioFinal)
class RelatorioFinalAdmin(admin.ModelAdmin):
    list_display = ('emailEmpresa', 'codFunc', 'descPentest')


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('cnpj', 'razaosocial', 'gerente', 'email')


@admin.register(Reuniao)
class ReuniaoAdmin(admin.ModelAdmin):
    list_display = ('data',  'hora', 'codFunc', 'email')