from django.shortcuts import render

from catalog.models import Product


# Create your views here.

def contacts(request):
    # реализация доп.задания
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f"{name} ({phone}, {email}): {message}")
    return render(request, 'catalog/contacts.html')

def home(request):
    context = {
        'object_list': Product.objects.all(),
    }
    return render(request, 'catalog/home.html', context)

def product(request, pk):
    product_item = Product.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(id=pk),
    }
    return render(request, 'catalog/product.html', context)

