# Generated by Django 4.0 on 2022-02-08 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Billofland',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_of_land', models.CharField(blank=True, max_length=50, null=True, verbose_name='Bill Of Land')),
                ('date', models.DateField(blank=True, null=True)),
                ('vendor', models.CharField(blank=True, max_length=50, null=True, verbose_name='Vendor')),
            ],
        ),
        migrations.CreateModel(
            name='Shelf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shelf', models.CharField(blank=True, max_length=50, null=True, verbose_name='Shelf')),
            ],
        ),
        migrations.CreateModel(
            name='OrderNumberShelf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_number_shelf', models.CharField(blank=True, max_length=50, null=True, verbose_name='Roll Number')),
                ('shelf', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cadastros.shelf')),
            ],
        ),
        migrations.CreateModel(
            name='Material_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PO_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='PO Number')),
                ('Order_number', models.CharField(blank=True, max_length=50, null=True, verbose_name='Order Number')),
                ('Side_Mark', models.CharField(blank=True, max_length=50, null=True, verbose_name=' SIdemark')),
                ('carrier', models.CharField(blank=True, choices=[('A.P.T. Distributing', 'A.P.T. Distributing'), ('Accurate Transport', 'Accurate Transport'), ('AllState', 'AllState'), ('APT', 'APT'), ('Belknap', 'Belknap'), ('Calhoun Distributio', 'Calhoun Distributio'), ('Carpenter', 'Carpenter'), ('Classic Tile', 'Classic Tile'), ('Couristan Carpets', 'Couristan Carpets'), ('Dalyn', 'Dalyn'), ('Dedicated LLC', 'Dedicated LLC'), ('Dixie', 'Dixie'), ('Elias Wilf', 'Elias Wilf'), ('Engineered', 'Engineered'), ('Fabrica', 'Fabrica'), ('Fishman', 'Fishman'), ('JJ Haines', 'JJ Haines'), ('Kane', 'Kane'), ('knae', 'knae'), ('Mannington', 'Mannington'), ('Masland', 'Masland'), ('Mohawk', 'Mohawk'), ('Nourtex/Nourison RU', 'Nourtex/Nourison RU'), ('PCC Ringgold', 'PCC Ringgold'), ('Phenix', 'Phenix'), ('Shaw', 'Shaw'), ('Southwind', 'Southwind'), ('Stanton', 'Stanton'), ('Stark', 'Stark'), ('UPS', 'UPS'), ('Urato', 'Urato')], max_length=50, null=True, verbose_name='Carrier')),
                ('Roll_number', models.CharField(blank=True, max_length=50, null=True, verbose_name=' Roll Number')),
                ('width', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('length', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('Quantity', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('take_out_date', models.DateField(blank=True, null=True, verbose_name='Take Out Date')),
                ('take_out_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Take Out Name')),
                ('material_type', models.CharField(blank=True, choices=[('Acessories', 'Acessories'), ('Area Rugs', 'Area Rugs'), ('Cabinet', 'Cabinet'), ('Carpet', 'Carpet'), ('Carpet Tile', 'Carpet Tile'), ('Ceilings', 'Ceilings'), ('Ceramic Tile', 'Ceramic Tile'), ('Displays', 'Displays'), ('Fixtures', 'Fixtures'), ('Installation Materials', 'Installation Materials'), ('Laminates', 'Laminates'), ('Pad', 'Pad'), ('Rubber Tile', 'Rubber Tile'), ('Runner', 'Runner'), ('Stone', 'Stone'), ('Training', 'Training'), ('Unclassified', 'Unclassified'), ('Vinyl', 'Vinyl'), ('Vinyl Sheet', 'Vinyl Sheet'), ('Vinyl Tile', 'Vinyl Tile'), ('Wall Base', 'Wall Base'), ('Wall Coverings', 'Wall Coverings'), ('wood', 'wood')], max_length=50, null=True, verbose_name='Material Type')),
                ('store', models.CharField(blank=True, choices=[('EB-Carpets & More East Brunswick', 'EB-Carpets & More East Brunswick'), ('Warehouse', 'Warehouse'), ('SI-Carpets & More Staten Island', 'SI-Carpets & More Staten Island'), ('OB-Carpets & More Old Bridge', 'OB-Carpets & More Old Bridge')], max_length=50, null=True, verbose_name='Corporation/Store')),
                ('barcode', models.ImageField(blank=True, upload_to='images/')),
                ('bill_of_land', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cadastros.billofland')),
            ],
        ),
    ]
