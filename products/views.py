from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})
from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

def product_upload(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirect to the product list after successful upload
    else:
        form = ProductForm()
    return render(request, 'products/product_upload.html', {'form': form})

from django.shortcuts import render

def product_list(request):
    return render(request, 'products/product_list.html')
