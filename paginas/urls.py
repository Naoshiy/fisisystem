from django.urls import path
from .views import PaginaInicial, Index 

urlpatterns = [
    # path('endereço/', IndezView(), name='nomedaurl')
    path('materialinfo', PaginaInicial.as_view(), name='materialinfo'),
    path('',Index.as_view(), name='home'),  
]