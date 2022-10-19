from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
def index(request):
    return render(request, 'accounts/index.html', {'infos': get_user_model().objects.all()})

def signup(request):
    form = CustomUserCreationForm(request.POST or None)
    if form.is_valid():
        login(request, form.save())
        return redirect('accounts:index')
    return render(request, 'accounts/signup.html', {'form': form})

def signin(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if form.is_valid():
        login(request, form.get_user())
        temp = None
        if request.GET.get('next'):
            temp = request.GET.get('next')
            if temp == '/articles/2/comment':
                temp = temp.replace('comment', 'detail')
        return redirect(temp or 'accounts:index')
    return render(request, 'accounts/login.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('articles:index')

def detail(request, pk):
    return render(request, 'accounts/detail.html', {'info': get_user_model().objects.get(pk=pk)})

@login_required
def mypage(request):
    return render(request, 'accounts/mypage.html')