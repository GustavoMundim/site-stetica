from django.db import models
from django.utils.safestring import mark_safe
# Create your models here.

class Perfil(models.Model):
    perfil_imagem = models.ImageField(upload_to='thumb-site')
    nome_perfil = models.CharField(max_length=50)
    descricao = models.TextField(max_length=1000)
    logo_site = models.ImageField(upload_to='thumb-site')

    class Meta:
        verbose_name = 'Configuração de Perfil Ajuste'

    @mark_safe
    def perfil_foto(self):
        return f'<img width="130px" src="/media/{self.perfil_imagem}">'
    
    def __str__(self):
        return 'Perfil de {}'.format(self.nome_perfil)



class Servicos(models.Model):
    imagem = models.ImageField(upload_to='thumb-site')
    servico = models.CharField(max_length=100)
    preco = models.FloatField()

    class Meta:
        verbose_name = 'Configuração de Servico Ajuste'

    @mark_safe
    def icon(self):
        return f'<img width="90px" src="/media/{self.imagem}">'



class AgendarServico(models.Model):
    imagem = models.ImageField(upload_to='thumb-site')

   
    
    class Meta:
        verbose_name = 'Configuração de Agendar Servico Ajuste'

    @mark_safe
    def imagem_fundo(self):
        return f'<img width="90px" src="/media/{self.imagem}">'


class AgendamentoSessao(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    servico_escolhido = models.CharField(max_length=100)
    horario_escolhido = models.CharField(max_length=300)
    
    class Meta:
        verbose_name = 'Serviços Agendado'

    def __str__(self):
        return "Cliente: {} {}".format(self.nome, self.sobrenome)


class Contato(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField()
    fundo_imagem = models.ImageField(upload_to='thumb-site')
    link_whatsaap = models.CharField(max_length=300)


    class Meta:
        verbose_name = 'Configuração de Contato Ajuste'

    @mark_safe
    def imagem_fundo(self):
        return f'<img width="90px" src="/media/{self.fundo_imagem}">'
    




class HorarioAjustes(models.Model):
    horarios = models.CharField(max_length=5)

    class Meta:
        verbose_name = 'Configuração de Horários Ajuste'

    def __str__(self):
        return self.horarios

class Profissao(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class AboutMe(models.Model):
    render_profile = models.ImageField(upload_to='thumb-site')
    descricao = models.TextField(max_length=800)
    page = 'Sobre mim pagina'

    class Meta:
        verbose_name = 'Configuração Sobre mim Ajuste'

    def __str__(self):
        return self.page


    @mark_safe
    def render_imagem(self):
        return f'<img width="90px" src="/media/{self.render_profile}">'

