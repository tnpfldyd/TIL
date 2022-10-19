from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
def signup(request):
    form = CustomUserCreationForm(request.POST or None)
    if form.is_valid():
        login(request, form.save())
        return redirect('articles:index')
    return render(request, 'accounts/signup.html', {'form':form})

def signin(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        login(request, form.get_user())
        return redirect(request.GET.get('next') or 'articles:index')
    return render(request, 'accounts/signin.html', {'form':form})

def signout(request):
    logout(request)
    return redirect('articles:index')

@login_required
def mypage(request):
    return render(request, 'accounts/mypage.html')