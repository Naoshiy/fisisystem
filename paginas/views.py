from django.views.generic import TemplateView

# Create your views here.

class PaginaInicial(TemplateView):
    template_name = "paginas/materialinfo.html"

class Index(TemplateView):
    template_name = "paginas/index.html"