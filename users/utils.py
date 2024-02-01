import random

from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse


def get_new_password():
    password_base = "abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789"
    password_base_list = list(password_base)
    abrakadabra = random.sample(password_base_list, 10)
    new_password = ''.join(abrakadabra)
    return new_password


def activate_user(request, token):
    key = get_object_or_404(User, token=token)
    current_user = User.objects.filter(is_active=False)
    for user in current_user:
        if str(user.token) == str(key):
            user.is_active = True
            user.token = None
            user.save()
    response = redirect('users/')
    return response

# def activate_user(request, token):
#
#     context = {
#         'title': "Подверждение",
#     }
#     if request.method == 'POST':
#         token = request.POST.get('token')
#         current_user = User.objects.filter(is_active=False)
#         for user in current_user:
#             if str(user.token) == str(token):
#                 user.is_active = True
#                 user.token = None
#                 user.save()
#     return render(request, 'users/verify.html', context)



def generate_new_password(request):
    # new_password  = ''.join([str(random.randint(0, 9)) for string in range(10)])

    new_password = get_new_password()
    send_mail(
        subject='Вы сменили пароль',
        message=f'Ваш новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    request.user.set_password(new_password)
    request.user.save()

    return redirect(reverse('users:login'))
