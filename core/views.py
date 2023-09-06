from django.views.generic import TemplateView
from .models import BoasVindas, Academico, Projetos, Certificados, Conhecimentos

# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"
    
    def get_context_data(self, **kwargs): 
        context = super(IndexView, self).get_context_data(**kwargs)
        context['boasvindas'] = BoasVindas.objects.all()
        context['academico'] = Academico.objects.all()
        context['principais'] = Projetos.objects.order_by('peso').all()
        context['certificados'] = Certificados.objects.order_by('?').all()
        context['conhecimentos'] = Conhecimentos.objects.all()
        return context
    

class ProjetosView(TemplateView):
    template_name = 'projetos.html'
    
    def get_context_data(self, **kwargs): 
        context = super(ProjetosView, self).get_context_data(**kwargs)
        context['projetos'] = Projetos.objects.all()
        return context