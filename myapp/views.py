from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Producto, Categoria, Stock
from .forms import ProductoForm

# Create your views here.

def hello(request):
    return HttpResponse("Hello World")

def about(request):
    return HttpResponse("About")

def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'registro.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def productos_list(request):
    productos = Producto.objects.all()
    return render(request, 'productos_list.html', {'productos' : productos})

def productos_list_admin(request):
    productos = Producto.objects.all()
    return render(request, 'prodadmin.html', {'productos': productos})

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.save()
            Stock.objects.create(cod_prod=producto, cantidad=form.cleaned_data['cantidad'])
            return redirect('prodadmin')
    else:
        form = ProductoForm()
    return render(request, 'agregar_producto.html', {'form': form})

def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.save()
            stock, created = Stock.objects.get_or_create(cod_prod=producto)
            stock.cantidad = form.cleaned_data['cantidad']
            stock.save()
            return redirect('prodadmin')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'editar_producto.html', {'form': form, 'producto': producto})

def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        return redirect('prodadmin')
    return render(request, 'eliminar_producto.html', {'producto': producto})