from django.shortcuts import render

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
    return render(request, 'catalog/home.html')