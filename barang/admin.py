from django.contrib import admin
from barang.models import *
# Register your models here.
admin.site.register(Kategori)
class ProdukAdmin(admin.ModelAdmin):
    list_display = ['nama', 'deskripsi', 'jumlah', 'Kategori']

admin.site.register(Produk, ProdukAdmin)