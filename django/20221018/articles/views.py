from django.shortcuts import render, redirect
from .forms import ArticleForm, CommentForm
from .models import Article,Comment
from django.contrib.auth.decorators import login_required
# Create your views here.
# app_name = 'articles'
# urlpatterns = [
#     path('',views.index, name='index'),
#     path('<int:pk>/',views.detail, name='detail'),
#     path('create/', views.create, name='create'),
#     path('<int:pk>/comments/', views.comments, name='comments'),
# ]

def index(request):
    contents = Article.objects.all()
    context = {
        'contents': contents,
    }
    return render(request, 'articles/index.html', context)

def detail(request, pk):
    context = {
        'article': Article.objects.get(pk=pk),
        'form': CommentForm(),
    }
    return render(request, 'articles/detail.html', context)
    
@login_required
def create(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        temp = form.save(commit=False)
        temp.user_id = request.user.id
        temp.save()
        return redirect('articles:index')
    return render(request, 'articles/create.html', {'form': form})

@login_required
def comments(request, pk):
    form = CommentForm(request.POST)
    if form.is_valid():
        temp = form.save(commit=False)
        temp.user_id = request.user.id
        temp.article_id = pk
        temp.save()
        return redirect('articles:detail', pk)

def comments_delete(request, article_pk, comment_pk):
    Comment.objects.get(pk=comment_pk).delete()
    return redirect('articles:detail', article_pk)