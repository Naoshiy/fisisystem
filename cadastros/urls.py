from unicodedata import name
from django.urls import path

from .views import   ShelfCreate, ShelfUpdate, article_list, create_material_form, detail_material, her, shelf_list 
from .views import MateriatypelUpdate, Material_typeDelete, BilloflandUpdate, BilloflandDelete
from .views import BilloflandList,Material_typeList

from . import views
from cadastros.views import create_material, ShelfCreate

urlpatterns = [
    #Example: path('admin/', admin.site.urls),
    # path('', include('paginas.urls -caminho-'))
    # path('register/billofland', her, name='billofland'),
    # path('register/billofland', BilloflandCreate.as_view(), name='billofland'),
    # path('register/materialtype', MaterialtypeCreate.as_view(), name='materialtype'),
    
    path('dbmaterial', Material_typeList.as_view(), name="dbmaterial"),   

    path('dbbill', BilloflandList.as_view(), name="dbbill"),
    path('tag', article_list, name="tag"),
    
    path('', views.index , name=""),
    path('create', views.create, name="create"),
 
    path('delete/material/<int:pk>', Material_typeDelete.as_view(), name='materialdelete'),
    path('billdelete/<int:pk>', BilloflandDelete.as_view(), name='billdelete'),

    path('materialupdate/<int:pk>/', MateriatypelUpdate.as_view(), name='materialupdate'),
    path('billupdate/<int:pk>/', BilloflandUpdate.as_view(), name='billupdate'),

    path('ff/<pk>/', create_material, name='createmat'),
    path('create-form/', create_material_form, name='create-form'), 
    # path('create-bill-form/', create_bill_form, name='create-bill-form'), 
    path('htmx/material', detail_material, name="detail-material"),  
    path('her', her, name="her"), 
    path('loc', ShelfCreate , name="loc"), 
    path('loclist', shelf_list , name="loclist"), 
    
    path('shelf/<int:pk>/', ShelfUpdate.as_view(), name='supdate'),
]
