from django.contrib import admin
from .models import Material_type, Billofland, Shelf, OrderNumberShelf

# Register your models here.
# admin.site.register(Material_type)
# admin.site.register(Billofland)

class MaterialInLineAdmin(admin.TabularInline):
    model = Material_type


class BillofladingAdmin(admin.ModelAdmin):
    inlines = [MaterialInLineAdmin]

admin.site.register(Billofland, BillofladingAdmin)

# ---------------------------------------------------------------------------


# admin.site.register(Shelf)
class RollShelfInLineAdmin(admin.TabularInline):
    model = OrderNumberShelf


class ShelfAdmin(admin.ModelAdmin):
    inlines = [RollShelfInLineAdmin]

admin.site.register(Shelf, ShelfAdmin)