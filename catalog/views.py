from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView, CreateView, DetailView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Version, Category
from catalog.services import get_cached_categories


# Create your views here.

def contacts(request):
    # реализация доп.задания
    context = {
        'title': "Контакты",
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f"{name} ({phone}, {email}): {message}")

    return render(request, 'catalog/contacts.html', context)


# def home(request):
#     context = {
#         'object_list': Product.objects.all(),
#     }
#     return render(request, 'catalog/home.html', context)

class HomeView(TemplateView):
    template_name = 'catalog/home.html'
    extra_context = {
        'title': "Каталог",
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Product.objects.all()
        if not self.request.user.is_staff:
            context_data['object_list'] = Product.objects.filter(is_published=True)
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
        # if not self.request.user.is_staff:
        #     queryset = queryset.filter(is_published=True)
        return queryset


class ProductDetailView(DetailView, PermissionRequiredMixin):
    model = Product
    permission_required = 'catalog.view_product'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(id=self.kwargs.get('pk'))
        return queryset


class ProductCreateView(CreateView, PermissionRequiredMixin):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')
    permission_required = 'catalog.add_product'

    # добавление автоматически продавца
    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProductUpdateView(UpdateView, PermissionRequiredMixin):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:home')
    permission_required = 'catalog.change_product'


    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SubjectFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)

        if self.request.method == "POST":
            context_data['formset'] = SubjectFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = SubjectFormset(instance=self.object)

        return context_data

    def form_valid(self, form):

        formset = self.get_context_data()['formset']
        self.object.save()

        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductDeleteView(DeleteView, PermissionRequiredMixin):
    model = Product
    success_url = reverse_lazy('catalog:home')
    permission_required = 'catalog.delete_product'


# @permission_required('catalog.view_version')
def version_active(request, pk):

    context = {
        'object_list': Version.objects.filter(product_id=pk, is_active=True),
    }

    return render(request, 'catalog/version_list.html', context)

class CategoryListView(LoginRequiredMixin, ListView):
    model = Category

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['category_list'] = get_cached_categories()
        return context_data
