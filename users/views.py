from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.conf import settings
from .forms import UserForm


class SignUpView(CreateView):
    template_name = 'signup.html'
    form_class = UserForm
    success_url = reverse_lazy('photo:list')

    def form_valid(self, form):
        to_return = super().form_valid(form)
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1']
        )

        login(self.request, user)

        send_mail(
            subject="Успешная авторизация!",
            message="Вы успешно авторизовались на нашем сайте! "
                    "Добро пожаловать!",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.request.user.email],
            fail_silently=False
        )

        return to_return


class UserLoginView(LoginView):
    template_name = 'login.html'


class UserLogoutView(LogoutView):
    pass
