from django.db import models
from django.db.models.deletion import PROTECT
from django.db.models.fields import CharField, DecimalField

#library def 3
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
from  django.core.files import File

# Create your models here.

class Billofland(models.Model):
    bill_of_land = models.CharField(max_length=50, verbose_name="Bill Of Land", null=True, blank=True)
    date = models.DateField( null=True, blank=True)
    vendor = models.CharField(max_length=50, verbose_name="Vendor", null=True, blank=True)
    def __str__(self):
        return  ("{} {} {}".format(self.bill_of_land,self.date,self.vendor))

class Material_type(models.Model):
    os_choice=(
        ('Acessories', 'Acessories'),
        ('Area Rugs', 'Area Rugs'),
        ('Cabinet', 'Cabinet'),
        ('Carpet', 'Carpet'),
        ('Carpet Tile','Carpet Tile'),
        ('Ceilings','Ceilings'),
        ('Ceramic Tile','Ceramic Tile'),
        ('Displays','Displays'),
        ('Fixtures','Fixtures'),
        ('Installation Materials','Installation Materials'),
        ('Laminates','Laminates'),
        ('Pad','Pad'),
        ('Rubber Tile','Rubber Tile'),
        ('Runner','Runner'),
        ('Stone','Stone'),
        ('Training','Training'),
        ('Unclassified','Unclassified'),
        ('Vinyl','Vinyl'),
        ('Vinyl Sheet','Vinyl Sheet'),
        ('Vinyl Tile','Vinyl Tile'),
        ('Wall Base','Wall Base'),       
        ('Wall Coverings','Wall Coverings'),       
        ('wood','wood'),       
    )
    os_choice1=(
        ('EB-Carpets & More East Brunswick', 'EB-Carpets & More East Brunswick'),
        ('Warehouse', 'Warehouse'),
        ('SI-Carpets & More Staten Island', 'SI-Carpets & More Staten Island'),
        ('OB-Carpets & More Old Bridge', 'OB-Carpets & More Old Bridge'),      
    )

    os_choice3 =(
        ('A.P.T. Distributing','A.P.T. Distributing'),
        ('Accurate Transport', 'Accurate Transport'),
        ('AllState','AllState'),
        ('APT','APT'),
        ('Belknap','Belknap'),
        ('Calhoun Distributio','Calhoun Distributio'),
        ('Carpenter','Carpenter'),
        ('Classic Tile','Classic Tile'),
        ('Couristan Carpets','Couristan Carpets'),
        ('Dalyn','Dalyn'),
        ('Dedicated LLC','Dedicated LLC'),
        ('Dixie','Dixie'),
        ('Elias Wilf','Elias Wilf'),
        ('Engineered','Engineered'),
        ('Fabrica','Fabrica'),
        ('Fishman','Fishman'),
        ('JJ Haines','JJ Haines'),
        ('Kane','Kane'),
        ('knae','knae'),
        ('Mannington','Mannington'),
        ('Masland','Masland'),
        ('Mohawk','Mohawk'),
        ('Nourtex/Nourison RU','Nourtex/Nourison RU'),
        ('PCC Ringgold','PCC Ringgold'),
        ('Phenix','Phenix'),
        ('Shaw','Shaw'),
        ('Southwind','Southwind'),
        ('Stanton','Stanton'),
        ('Stark','Stark'),
        ('UPS','UPS'),
        ('Urato','Urato'),
    )

    bill_of_land = models.ForeignKey(Billofland, on_delete=models.CASCADE,  null=True, blank=True)
    # shelf_fk = models.ForeignKey(Shelf, on_delete=models.CASCADE,  null=True, blank=True)
    
    #   bill_of_land = models.   

    PO_number = models.CharField(max_length=50, verbose_name="PO Number", null=True, blank=True)
    Order_number = models.CharField(max_length=50, verbose_name="Order Number", null=True, blank=True)
    Side_Mark = models.CharField(max_length=50, verbose_name=" SIdemark", null=True, blank=True)
    carrier = models.CharField(max_length=50, choices=os_choice3, verbose_name="Carrier", null=True, blank=True)
    Roll_number = CharField(max_length=50, verbose_name=" Roll Number", null=True, blank=True)
    width = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    length = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    Quantity = models.DecimalField(max_digits=30, decimal_places=2, null=True, blank=True)
    take_out_date = models.DateField(null=True, verbose_name="Take Out Date",  blank=True) 
    take_out_name = models.CharField(max_length=50, verbose_name="Take Out Name", null=True, blank=True)
    material_type = models.CharField(max_length=50, choices=os_choice, verbose_name="Material Type", null=True, blank=True)
    store = models.CharField(max_length=50, choices=os_choice1, verbose_name="Corporation/Store", null=True, blank=True)
    barcode = models.ImageField(upload_to='images/', blank=True)
    
    def __str__(self):
        return  ("{} {} {} {} {} {} {} {} {} {} {} {}".format(self.PO_number, self.material_type, self.store, self.Order_number, 
        self.Side_Mark, self.Roll_number, self.width, self.length, self.Quantity, self.take_out_date, self.take_out_name, self.carrier, self.barcode))


#def 3
    def save(self, *args, **kwargs):
        EAN = barcode.get_barcode_class('code128')
        ean = EAN(f'{self.Roll_number}', writer=ImageWriter())
        buffer = BytesIO()
        ean.write(buffer)
        # self.barcode.save(f'{self.barcode}.png', File(buffer), save=False)
        self.barcode.save(f'barcode.png', File(buffer), save=False)
        return super().save(*args, **kwargs)    


class Shelf(models.Model):
    shelf = models.CharField(max_length=50, verbose_name="Shelf", null=True, blank=True)
    def __str__(self):
        return  ("{}".format(self.shelf))
    
class OrderNumberShelf(models.Model):
    roll_number_shelf = models.CharField(max_length=50, verbose_name="Roll Number", null=True, blank=True)
    shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE,  null=True, blank=True)
    def __str__(self):
        return  ("{} ".format(self.roll_number_shelf))
    
    