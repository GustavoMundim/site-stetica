from django.contrib import admin
from .models import Servicos, AgendarServico, Contato, AgendamentoSessao, Perfil, HorarioAjustes, AboutMe
from django.http import HttpResponse
# Register your models here.

@admin.register(Perfil)
class PerfilView(admin.ModelAdmin):
    list_display = ('perfil_foto', 'nome_perfil', 'descricao', 'logo_site')
    list_editable = ('nome_perfil', 'descricao')

 
    

@admin.register(Servicos)
class ServicoView(admin.ModelAdmin):
    list_display = ('icon', 'servico', 'preco')
    list_editable = ('preco',)

@admin.register(AgendarServico)
class AgendamentoView(admin.ModelAdmin):
    list_display = ('imagem_fundo',)


@admin.register(Contato)
class ContatoView(admin.ModelAdmin):
    list_display = ('imagem_fundo', 'nome', 'sobrenome', 'email', 'link_whatsaap')
    list_editable = ('nome', 'sobrenome', 'email', 'link_whatsaap')

@admin.register(AgendamentoSessao)
class AgendamentoView(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'servico_escolhido', 'horario_escolhido')


@admin.register(HorarioAjustes)
class TimeView(admin.ModelAdmin):
    list_display = ['horarios']
    list_editable = ['horarios']
    list_display_links = None


@admin.register(AboutMe)
class SobreMimView(admin.ModelAdmin):
    list_display = ['render_imagem', 'descricao']
    list_editable = ['descricao']





