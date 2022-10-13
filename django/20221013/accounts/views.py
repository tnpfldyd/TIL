from django.shortcuts import render, redirect
from .forms import CustomUsercreationForm, CustomUserChangeForm
from django.contrib.auth import login, logout
from django.contrib.auth import get_user_model,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    infos = get_user_model().objects.all()
    context = {
        'infos': infos
    }
    return render(request, 'accounts/index.html', context)

def signup(request):
    form = CustomUsercreationForm(request.POST or None)
    if form.is_valid():
        login(request, form.save())
        return redirect('accounts:index')
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

def detail(request, pk):
    info = get_user_model().objects.get(pk=pk)
    context = {
        'info': info,
    }
    return render(request, 'accounts/detail.html', context)

def signin(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        login(request, form.get_user())
        return redirect(request.GET.get('next') or 'accounts:index')
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

@login_required
def signout(request):
    logout(request)
    return redirect('accounts:index')

@login_required
def update(request, pk):
    form = CustomUserChangeForm(request.POST or None, instance=request.user)
    if form.is_valid():
        form.save()
        return redirect('accounts:index')
    context = {
        'form': form
    }
    return render(request, 'accounts/update.html', context)


@login_required
def password(request):
    form = PasswordChangeForm(request.user, request.POST or None)
    if form.is_valid():
        form.save()
        update_session_auth_hash(request, form.user)
        return redirect('accounts:index')
    context = {
        'form': form,
    }
    return render(request, 'accounts/password.html', context)

@login_required
def delete(request):
    request.user.delete()
    logout(request)
    return render(request, 'accounts/index.html')