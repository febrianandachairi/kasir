from django.shortcuts import render, redirect
#Manggil data dari database
from barang.models import *

# Create your views here.
def barang_list(request):
    template_name = 'barang_list.html'
    produk_list = Produk.objects.all()
    context = {
        'title' : 'Ini halaman Barang',
        'produk' : produk_list
    }
    return render(request, template_name, context)
def barang_add(request):
    template_name = 'barang_add.html'
    kategori_data = Kategori.objects.all()

    if request.method == "POST":
        input_nama = request.POST.get('nama')
        input_kategori = request.POST.get('kategori')
        input_jumlah = request.POST.get('jumlah')
        input_deskripsi = request.POST.get('deskripsi')
    
        #panggil kategori terlebih dahulu karena memiliki relasi
        get_kategori = Kategori.objects.get(nama=input_kategori)

        Produk.objects.create(
            nama = input_nama,
            deskripsi = input_deskripsi,
            jumlah = input_jumlah,
            Kategori = get_kategori,
        )
        return redirect(barang_list)
    context = {
        'title' : 'Ini halaman tambah Barang',
        'kategori' : kategori_data
    }
    print("Simpan/Tambah Data")
    return render(request, template_name, context)
def barang_update(request, id):
    template_name = 'barang_add.html'
    kategori_data= Kategori.objects.all()
    get_produk = Produk.objects.get(id=id)
    if request.method == "POST":
        input_nama = request.POST.get('nama')
        input_kategori = request.POST.get('kategori')
        input_jumlah = request.POST.get('jumlah')
        input_deskripsi = request.POST.get('deskripsi')
    
        #panggil kategori terlebih dahulu karena memiliki relasi
        get_kategori = Kategori.objects.get(nama=input_kategori)

        get_produk.nama = input_nama
        get_produk.Kategori = get_kategori
        get_produk.jumlah = input_jumlah
        get_produk.deskripsi = input_deskripsi
        get_produk.save()
        
        return redirect(barang_list)
        print("Update/Edit Data")
    
    context = {
        'title' : 'ini halaman Update barang',
        'kategori' : kategori_data,
        'get_produk' : get_produk, 
    }
    print("Update/Edit Data")

    return render(request, template_name, context)

def barang_delete(request, id):
    get_produk = Produk.objects.get(id=id).delete()
    print("Delete Data")
    return redirect(barang_list)


