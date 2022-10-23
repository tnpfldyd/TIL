from django.shortcuts import render, redirect
from .forms import ArticleForm, CommentForm
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from django.http import HttpResponseForbidden, HttpResponse
from django.contrib import messages
import os
# Create your views here.
def index(request):
    return render(request, 'articles/index.html', {'contents': Article.objects.all()})

@login_required
def create(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        temp = form.save(commit=False)
        temp.user_id = request.user.id
        temp.save()
        return redirect('articles:detail', temp.id)
    return render(request, 'articles/create.html', {'form': form})

def detail(request, pk):
    print(request)
    context = {
        'article': Article.objects.get(pk=pk),
        'form': CommentForm()
    }
    return render(request, 'articles/detail.html', context)

@login_required
def comment(request, article_pk):
    form = CommentForm(request.POST)
    if form.is_valid():
        temp = form.save(commit=False)
        temp.article_id = article_pk
        temp.user_id = request.user.id
        temp.save()
        return redirect('articles:detail', article_pk)

@login_required
def comment_delete(request, article_pk, comment_pk):
    temp = Comment.objects.get(pk=comment_pk)
    if request.user.id == temp.user_id:
        temp.delete()
        return redirect('articles:detail', article_pk)
    else:
        return HttpResponseForbidden

@login_required
def update(request, pk):
    temp = Article.objects.get(pk=pk)
    if request.user.id == temp.user_id:
        form = ArticleForm(request.POST or None, request.FILES or None, instance=Article.objects.get(pk=pk))
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
    else:
        return HttpResponseForbidden
        
@login_required
def delete(request, pk):
    temp = Article.objects.get(pk=pk)
    if request.user.id == temp.user_id:
        if temp.image:
            os.remove(temp.image.path)
        if temp.thumbnail:
            os.remove(temp.thumbnail.path)
        Article.objects.get(pk=pk).delete()
        return redirect('articles:index')
    else:
        return HttpResponseForbidden