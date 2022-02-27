from django import forms
from .models import Billofland, Material_type, Shelf, OrderNumberShelf

from cadastros.models import Billofland , Material_type

# from django.forms.models import inlineformset_factory

class BilloflandForms(forms.ModelForm):
    class Meta:
        model = Billofland
        fields = ('bill_of_land','date','vendor')
  

class Material_typeForms(forms.ModelForm):
    class Meta:
        model = Material_type
        fields = "__all__"
        exclude = ['bill_of_land_key']

        
from django.forms.models import inlineformset_factory

MaterialFormSet = inlineformset_factory(
    Billofland,
    Material_type,
    form=Material_typeForms,
    min_num=2,  # minimum number of forms that must be filled in
    extra=1,  # number of empty forms to display
    can_delete=True  # show a checkbox in each form to delete the row
)

class ShelfForm(forms.ModelForm):
    class Meta:
        model = Shelf
        fields = "__all__"
        
class MaterialShelfForms(forms.ModelForm):
    class Meta:
        model = OrderNumberShelf
        fields="__all__"
