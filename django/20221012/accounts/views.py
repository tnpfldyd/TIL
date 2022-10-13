from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def index(request):
    infos = get_user_model().objects.all()
    context = {
        'infos': infos
    }
    return render(request, 'accounts/index.html', context)

def signup(request):
    form = CustomUserCreationForm(request.POST or None)
    if form.is_valid():
        login(request, form.save())
        return redirect('accounts:index')
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

@login_required
def detail(request, pk):
    info = get_user_model().objects.get(pk=pk)
    context = {
        'info': info
    }
    return render(request, 'accounts/detail.html', context)

def signin(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        login(request, form.get_user())
        return redirect(request.GET.get('next') or 'main')
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

def signout(request):
    logout(request)
    return redirect('main')