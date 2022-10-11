from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)
def index(request):
    infos = get_user_model().objects.all()
    context = {
        'infos': infos,
    }
    return render(request, 'accounts/index.html', context)

def detail(request, pk):
    info = get_user_model().objects.get(pk=pk)
    context = {
        'info': info,
    }
    return render(request, 'accounts/detail.html', context)