from django.shortcuts import render,redirect
from .forms import ArticleForm
from .models import Article
import math

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')
def board(request, num):
    temp = Article.objects.order_by('-updated_at')[(num-1)*15:num*15]
    btn = math.ceil(Article.objects.all().count()/15)
    btn_tong = []
    for i in range(1, btn+1):
        btn_tong.append(i)
    context = {
        'temps': temp,
        'btns': btn_tong,
    }
    return render(request, 'articles/board.html', context)
def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:board', 1)
    else:    
        article_form = ArticleForm()
    context = {
        'article_form':article_form,
    }
    return render(request, 'articles/create.html', context=context)

def detail(request, pk):
    info = Article.objects.get(pk=pk)
    context = {
        'info': info,
    }
    return render(request, 'articles/detail.html', context)

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:detail', article.pk)
    else:
        article_form = ArticleForm(instance=article)
    context = {
        'article_form': article_form,
        'article': article,
    }
    return render(request, 'articles/edit.html', context)