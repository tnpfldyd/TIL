from django.shortcuts import render, redirect
from accounts.models import CustomEmail
from .forms import CustomUsercreationForm, CustomUserChangeForm
from django.contrib.auth import login, logout
from django.contrib.auth import get_user_model,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .forms import CustomEmailForm
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
        print(request.GET)
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

@login_required
def email_send(request, send_pk):
    if request.method == 'POST':
        form = CustomEmailForm(request.POST, request.FILES)
        info = get_user_model().objects.get(pk=send_pk)
        print(request.POST,request.FILES)
        if form.is_valid():
            from_info = get_user_model().objects.filter(email=request.POST['to_email_address'])
            for i in from_info:
                temp = form.save(commit=False)
                temp.recipient_id = i.id
                temp.from_name = info.username
                temp.from_email = info.email
                temp.save()
            return redirect('accounts:index')
    else:
        form = CustomEmailForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/email_send.html', context)

@login_required
def email_box(request, pk):
    print(request.user.id)
    info = get_user_model().objects.get(pk=pk)
    temp = CustomEmail.objects.filter(recipient_id=info.pk)
    context = {
        'info': info,
        'temp': temp,
    }
    return render(request, 'accounts/email_box.html', context)