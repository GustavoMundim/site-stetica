from typing import Any
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, View
from .models import Servicos, AgendarServico, Contato, AgendamentoSessao, Perfil, HorarioAjustes, AboutMe
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.


class HomePage(ListView):
    model = Servicos
    template_name = 'homepage.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['perfil'] = Perfil.objects.all()
        context['active_page'] = 'homepage'
        context['about'] = AboutMe.objects.all()
        return context
    


    


class Agendamento(TemplateView):
    template_name = 'agendamento.html'
    status = {}
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['consultar'] = Servicos.objects.all()
        context['foto_fundo'] = AgendarServico.objects.all()
        context['horarios'] = list(HorarioAjustes.objects.values_list('horarios', flat=True))
        context['active_page'] = 'agendamento'
        context['status'] = self.request.GET.dict()
        context['horarios_ocupado'] = list(AgendamentoSessao.objects.values_list('horario_escolhido', flat=True))
        return context
    
    def post(self, request):
        self.nome = request.POST.get('nome').capitalize()
        self.sobrenome = request.POST.get('sobrenome').capitalize()
        self.servico = request.POST.get('servico')
        self.horario_marcado = request.POST.get('horario-marcado')
        return self.verificar_nome()
    
    def cadastro_formulario(self):
        cadastrar_formulario = AgendamentoSessao(nome = self.nome, sobrenome= self.sobrenome, servico_escolhido = self.servico, horario_escolhido = self.horario_marcado)
        cadastrar_formulario.save()
    
    
    def verificar_nome(self):
        verificacao = AgendamentoSessao.objects.filter(nome = self.nome).filter(sobrenome = self.sobrenome)
        if verificacao.exists():
            verificacao.delete()
            self.cadastro_formulario()
            return redirect(reverse('site-estetica:agendamento')  + '?status=0')
        else:
            return self.verificar_formulario()
        
    def verificar_formulario(self):
        if len(self.nome.strip()) == 0 or len(self.sobrenome.strip()) == 0:
            return redirect(reverse('site-estetica:agendamento')  + '?status=2')
        else:
            self.cadastro_formulario()
            return redirect(reverse(f'site-estetica:agendamento')  + '?status=1')

def test_site(request):
    return render(request, 'test.html')
    

        


    
class AgendamentoSelecionado(Agendamento):
    template_name = 'agendamento-selecionado.html'
    link_site = 'agendamento-escolhido'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs['id']
        context['escolhido'] = Servicos.objects.get(id=id)
        return context
    
    def post(self, request, **kwargs):
       return super().post(request)
        
    



def contato(request):
    active_page = 'contato'
    ajuste = Contato.objects.first()
    return render(request, 'contato.html', {'active_page': active_page, 'contato_ajuste': ajuste})


def galeria_site(request):
    active_page = 'galeria'
    return render(request, 'galeria.html', {'active_page': active_page})





    
