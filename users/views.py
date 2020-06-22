from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login
from .forms import *
from django.contrib import messages
from django.http import HttpResponse


# Create your views here.
def register_page(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            messages.success(request, 'Аккаунт успешно  зарегистрирован! Теперь вы можете войти.')
            return redirect('login_page_url')
    else:
        form = RegistrationForm()
    return render(request, 'users/register_page.html', context={'form': form})


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, 'С возвращением!')
                return redirect('main_page_url')
            else:
                return HttpResponse('Disabled account')
    else:
        form = LoginForm()
    return render(request, 'users/login_page.html', context={'form': form})
