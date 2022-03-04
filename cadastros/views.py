
from ast import parse
from dataclasses import field
from datetime import date, timedelta
from multiprocessing import active_children, context
from pdb import post_mortem
from unicodedata import category
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Billofland
from django.urls import reverse_lazy 

###-------------------------------------------------------
from django.shortcuts import render, redirect
from django.contrib import messages

from django.http import HttpResponseRedirect
from .models import Billofland, Material_type
from .models import *

from django.forms.models import inlineformset_factory
from cadastros.forms import  Material_typeForms 
from cadastros.models import Billofland, Material_type
from cadastros.forms import BilloflandForms




       
## LISTA ###       
class BilloflandList(ListView):
    model = Billofland
    template_name = 'cadastros/dbbill.html'
    
class tagList(ListView):
    model = Material_type
    template_name = 'cadastros/pdf.html'
    
class Material_typeList(ListView):
    model = Material_type
    template_name = 'cadastros/db.html'


### UPDATE ###
class MateriatypelUpdate(UpdateView):
    model = Material_type
    # fields = ['bill_of_land', 'PO_number', 'Order_number', 'Side_Mark', 'Roll_number', 'Quantity', 'width', 'length', 'take_out_date', 'take_out_name', 'material_type', 'store', 'carrier']
    fields = "__all__"
    template_name = 'cadastros/forms.html'
    success_url = reverse_lazy('dbmaterial')

class BilloflandUpdate(UpdateView):
    model = Billofland
    fields = "__all__"
    template_name = 'cadastros/forms.html'
    success_url = reverse_lazy('dbbill')

# update take out


### DELETE ###
class Material_typeDelete(DeleteView):
    model = Material_type
    template_name = 'cadastros/delete.html'
    success_url = reverse_lazy('dbmaterial')

class BilloflandDelete(DeleteView):
    model = Billofland
    template_name = 'cadastros/delete.html'
    success_url = reverse_lazy('dbbill')


def inner(request):
    uni = Material_type.objects.all().select_related('bill_of_land')
    return render(request,'cadastros/pdf.html', {'uni': uni })
  


from django.shortcuts import render
from .models import  Material_type
from django.http import HttpResponse

def index(request):
    
    return render(request, 'forms1.html')

        
# https://stackoverflow.com/questions/26855631/javascript-to-django-views-py/26858442
def create(request):
    if request.method=='POST':
        bill_of_land:request.POST['bill_of_land']
        date :request.POST['date ']
        vendor:request.POST['vendor']
        new_profile = Material_type(bill_of_land=bill_of_land, date =date, vendor=vendor )
        new_profile.save()
        success = 'material created'
        return HttpResponse(success)

# ----------------------------------------------------

# pip install django-Widget-tweaks - filters: https://www.youtube.com/watch?v=r07P2npmOAw
# https://www.youtube.com/watch?v=grsZ5yO9eVg - pt 3

# https://www.youtube.com/watch?v=sqhQM5KUFHE - Calendar filter


import django_filters
def article_list(request):
    
    template_name = 'cadastros/pdf.html'
    object_list = Material_type.objects.all().select_related('bill_of_land')
      
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    carrier = request.GET.get('carrier')
    Roll_number = request.GET.get('Roll_number')
    if start_date and end_date:
        object_list = object_list.filter(bill_of_land__date__range=[start_date, end_date])
    elif Roll_number:
        object_list = object_list.filter(Roll_number=Roll_number)
    elif carrier:
        object_list = object_list.filter(carrier=carrier)
    else:
        # object_list = Material_type.objects.all().select_related('bill_of_land')
        object_list =[]

    context = {
        'object_list': object_list,
            }
    
    return render(request, template_name, context)
    
    
    
def create_material(request, pk):
    author = Billofland.objects.get(id=pk)
    books = Material_type.objects.all() #.filter(author=author)
    
    MaterialFormset = inlineformset_factory(
        Billofland, Material_type, 
        form = Material_typeForms,
        extra=0, 
        can_delete=False, 
        validate_min=True)
    
    form = Material_typeForms(request.POST or None)
    formset = BilloflandForms(request.POST or None)

    if request.method == "POST":
        if form.is_valid() and formset.is_valid():
            book = form.save(commit=False)
            formset = formset.save(commit=False)
            book.author = author
            book.save()
            formset.save()
            # return HttpResponse("success")
            return redirect("detail-material", pk=book.id)
        else:
            return render(request, "cadastros/material_form.html", context={
                "form": form
            })

    context = {
        "formset":formset,
        "form": form,
        "author": author,
        "books": books
    }

    return render(request, "cadastros/form.html", context)

def her(request):
    her_forms = Billofland() 
    MaterialFormset = inlineformset_factory(
        Billofland, Material_type, 
        form = Material_typeForms, 
        extra=0, 
        can_delete=False, 
        validate_min=True)

    if request.method == 'POST':
           forms = BilloflandForms(request.POST, request.FILES, instance=her_forms, prefix='main')
           formset = MaterialFormset(request.POST, request.FILES, instance=her_forms, prefix='product')

           if forms.is_valid() and formset.is_valid():
               forms = forms.save(commit=False)
               forms.save()
               formset.save()
               return HttpResponseRedirect('her')
            #    return redirect("detail-material")
           else:
                return render(request, "cadastros/material_form.html", context={
                "form": forms
            })

    else:
        forms = BilloflandForms(instance=her_forms, prefix='main')
        formset = MaterialFormset(instance=her_forms, prefix='product')

    context = {
        'forms': forms,
        'formset': formset,
    }
    context['loop_times'] = range(1,20)
    return render(request, 'cadastros/forms1.html', context)
    
    
from .forms import AnexoForms, Material_typeForms, MaterialShelfForms, ShelfForm


def create_material_form(request):
    form = Material_typeForms() 
    context = {
        "form": form
    }
    return render(request, "cadastros/material_form.html", context)


from django.shortcuts import get_object_or_404

def detail_material(request, pk):
    book = get_object_or_404(Material_type, id=pk)
    # bill = get_object_or_404(Billofland, id=pk)
    context = {
        # 'bill':bill,
        "book": book
    }
    return render(request, "cadastros/material_detail.html", context)

# ------------ shelf ------------------------------------

def ShelfCreate(request):
    shelf = Shelf() 
    ShelfFormset = inlineformset_factory(
        Shelf, OrderNumberShelf, 
        form = MaterialShelfForms, 
        extra=0, 
        can_delete=False, 
        validate_min=True)

    if request.method == 'POST':
           forms_shelf = ShelfForm(request.POST, request.FILES, instance=shelf, prefix='main')
           formset_shelf = ShelfFormset(request.POST, request.FILES, instance=shelf, prefix='product')

           if forms_shelf.is_valid() and formset_shelf.is_valid():
               forms_shelf = forms_shelf.save(commit=False)
               forms_shelf.save()
               formset_shelf.save()
               return HttpResponseRedirect('loc')
            #    return redirect("detail-material")
        #    else:
        #         return render(request, "cadastros/material_form.html", context={
        #         "form": forms
        #     })

    else:
        forms_shelf = ShelfForm(instance=shelf, prefix='main')
        formset_shelf = ShelfFormset(instance=shelf, prefix='product')

    context = {
        'forms_shelf': forms_shelf,
        'formset_shelf': formset_shelf,
    }

    return render(request, 'cadastros/location.html', context)



def shelf_list(request):
    
    template_name = 'cadastros/location_list.html'
    shelf_list = OrderNumberShelf.objects.all().select_related('shelf').select_related('sm')
    # start_date = request.GET.get('start_date')
    # end_date = request.GET.get('end_date')
    Roll_number = request.GET.get('Roll_number')
    # if start_date and end_date:
    #     shelf_list = shelf_list.filter(bill_of_land__date__range=[start_date, end_date])
    if Roll_number:
        shelf_list = shelf_list.filter(Roll_number=Roll_number)
    else:
        shelf_list = OrderNumberShelf.objects.all().select_related('shelf')

    context = {
        'shelf_list': shelf_list,
            }
    
    return render(request, template_name, context)


### UPDATE ###
class ShelfUpdate(UpdateView):
    model = OrderNumberShelf
    fields = ['roll_number_shelf']
    template_name = 'cadastros/location.html'
    success_url = reverse_lazy('loc')
    
# anexo
def create_anexo_form(request):
    form_anexo = AnexoForms() 
    context = {
        "form_anexo": form_anexo
    }
    return render(request, "cadastros/db.html", context)
    

    
    
    