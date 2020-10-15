from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate, get_user_model
from django.contrib import messages
from .forms import LoginForm, RegisterForm
# Create your views here.


def logoutview(request):
    logout(request)
    return redirect('accounts:login')


def loginview(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                messages.success(request, f'Welcome Back {username}!')
                return redirect('todo:home')
            else:
                messages.success(request, f'Sorry, Account has been Deactivated')
                return redirect('accounts:login')
        else:
            messages.success(request, f'Invalid Credentials')
            return redirect('accounts:login')
    name = 'login.html'
    context = {
        'form' : form
    }
    return render(request, name, context)


User = get_user_model()
def registerview(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        data = form.cleaned_data
        User.objects.create_user(username=data['username'], password=data['password'], email=data['email'])
        messages.success(request, 'Account Created Successfully')
        return redirect('accounts:login')
    name = 'login.html'
    context = {
        'form' : form
    }
    return render(request ,name, context)