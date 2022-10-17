import os
from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import Profile
# Create your views here.

def index(request):
    return render(request, 'articles/index.html', {'contents': Profile.objects.all()})

def create(request):
    form = ProfileForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('articles:index')
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)

def detail(request, pk):
    return render(request, 'articles/detail.html', {'content': Profile.objects.get(pk=pk)})
    
def update(request, pk):
    temp = Profile.objects.get(pk=pk)
    form = ProfileForm(request.POST or None, request.FILES or None, instance=Profile.objects.get(pk=pk))
    if form.is_valid():
        if (temp.image and request.FILES.get('image')) or request.POST.get('image-clear'):
            os.remove(temp.image.path)
        if (temp.thumbnail and request.FILES.get('thumbnail')) or request.POST.get('thumbnail-clear') :
            os.remove(temp.thumbnail.path)
        form.save()
        return redirect('articles:detail', pk)
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)

def delete(request, pk):
    temp = Profile.objects.get(pk=pk)
    if temp.image:
        os.remove(temp.image.path)
    if temp.thumbnail:
        os.remove(temp.thumbnail.path)
    Profile.objects.get(pk=pk).delete()
    return redirect('articles:index')
