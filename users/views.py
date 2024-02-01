import random

from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    # особенность на почту @gmail.com - письма не доходят, но на @mail.ru - работает
    # Регистрация подвисает, несколько секунд. Иногда, регистрация - так и весит.
    # Потом пробую вести - уже существует, И есть кнопка войти. и вход возможен.
    # def form_valid(self, form):
    #     new_user = form.save()
    #     send_mail(
    #         subject='Поздравляем с регистрацией',
    #         message='Вы зарегистрировались на нашей платформе! Добро Пожаловать!',
    #         from_email=settings.EMAIL_HOST_USER,
    #         recipient_list=[new_user.email]
    #     )
    #
    #     return super().form_valid(form)

    def form_valid(self, form):
        new_user = form.save()
        new_user.is_active = False
        secret_token = ''.join([str(random.randint(0, 9)) for string in range(10)])
        new_user.token = secret_token
        message = f'Вы указали этот E-mail в качестве основного адреса на нашей платформе!\nДля подтверждения вашего Е-mail перейдите по ссылке https://127.0.0.1:8000/verify/{secret_token}'
        send_mail(
            subject='Подтверждение E-mail адреса',
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )

        return super().form_valid(form)


class ProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):  # тем самым уходим от привязки с pk
        return self.request.user


