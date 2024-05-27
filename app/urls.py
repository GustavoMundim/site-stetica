from django.urls import path, include
from . import views


app_name = 'site-estetica'

urlpatterns = [
    path('', views.HomePage.as_view(), name='homepage'),
    path('agendar/', views.Agendamento.as_view(), name='agendamento'),
    path('agendar/<int:id>', views.AgendamentoSelecionado.as_view(), name='agendamento-selecionado'),
    path('contato/', views.contato, name='contato'),
    path('galeria', views.galeria_site, name='galeria'),
    path('test/', views.test_site, name='test')
    ]