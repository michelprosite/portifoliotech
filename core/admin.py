from django.contrib import admin
from .models import BoasVindas, Academico, Projetos, Certificados, Conhecimentos

# Register your models here.
@admin.register(BoasVindas)
class BoasVindasAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'mensagem', 'link', 'textButtom', 'ativo']
    

@admin.register(Academico)
class AcademicoAdmin(admin.ModelAdmin):
    list_display = ['curso', 'instituicao', 'dataInicio', 'dataConclusao', 'textButtom', 'ativo']
    
    
@admin.register(Projetos)
class ProjetosAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'urlgit', 'urlsite', 'dataConclusao', 'cargaHoraria', 'peso', 'ativo']
    
    
@admin.register(Certificados)
class CertificadoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'instituicao', 'dataConclusao', 'cargaHoraria', 'ativo']
    
    
@admin.register(Conhecimentos)
class ConhecimentosAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'nivel', 'icone', 'ativo']