from django.shortcuts import render
from django.views.generic import ListView, TemplateView

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

# def home(request):
#     context = {
#         'object_list': Product.objects.all(),
#     }
#     return render(request, 'catalog/home.html', context)

class HomeView(TemplateView):
    template_name = 'catalog/home.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data ['object_list'] = Product.objects.all()
        return context_data

# def product(request, pk):
#     product_item = Product.objects.get(pk=pk)
#     context = {
#         'object_list': Product.objects.filter(id=pk),
#     }
#     return render(request, 'catalog/product_list.html', context)

class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(id=self.kwargs.get('pk'))
        return queryset
        
