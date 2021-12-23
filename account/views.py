from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404

#Регистрация
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView

from account.forms import RegistrationForm, ChangePasswordForm, ForgotPasswordForm, ForgotPasswordCompleteForm

User = get_user_model()


class RegisterView(View):
    form_class = RegistrationForm
    template_name = 'account/registration.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('register-success'))
        return render(request, self.template_name, {'form': form})


class SuccessfulRegistrationView(TemplateView):
    template_name = 'account/successful_registration.html'


# Активация
class ActivationView(View):
    def get(self, request, *args, **kwargs):
        code = kwargs.get('code')
        # user = User.objects.get(activation_code=code)
        user = get_object_or_404(User, activation_code=code)
        user.is_active = True
        user.activation_code = ''
        user.save()
        return render(request, 'account/activation.html')


class SigninView(LoginView):
    template_name = 'account/login.html'


# Смена пароля
class ChangePasswordView(LoginRequiredMixin, View):
    template_name = 'account/change_password.html'
    form_class = ChangePasswordForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(request=request)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request=request)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('products-list'))
        return render(request, self.template_name, {'form': form})


# Восстановление пароля
class ForgotPasswordView(View):
    form_class = ForgotPasswordForm
    template_name = 'account/forgot_password.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.send_mail()
            return redirect(reverse_lazy('forgot-password-complete'))
        return render(request,self.template_name, {'form': form})


class ForgotPasswordCompleteView(View):
    form = ForgotPasswordCompleteForm
    template_name = 'account/forgot_password_complete.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('products-list'))
        return render(request, self.template_name, {'form': form})

    # TODO: сверстать все страницы





