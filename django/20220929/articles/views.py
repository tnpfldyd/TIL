from django.shortcuts import render,redirect
from .models import Articles
import math
# Create your views here.
def root(request):
    return render(request, 'articles/root.html')
def main(request, num):
    title = Articles.objects.order_by('-id')[(num-1)*15:num*15]
    btn = math.ceil(Articles.objects.all().count()/15)
    result = []
    for i in range(1, btn + 1):
        result.append(i)

    context = {
        'articles': title,
        'result': result,
    }
    return render(request, 'articles/main.html', context)
def create(request):
    return render(request, 'articles/create.html')
def detail(request, pk):
    temp = Articles.objects.get(pk=pk)
    context = {
        'temp': temp,
    }
    return render(request, 'articles/detail.html', context)
def create2(request):
    temp = request.GET
    Articles.objects.create(title=temp['title'], content=temp['content'], password=temp['password'])
    return redirect('articles:main',1)
def edit(request, pk):
    temp = Articles.objects.get(pk=pk)
    context = {
        'temp': temp,
    }
    return render(request, 'articles/edit.html', context)
def edit2(request, pk):
    temp = Articles.objects.get(pk=pk)
    edit = request.GET
    temp.title = edit['title']
    temp.content = edit['content']
    temp.save()
    return redirect('articles:main',1)
def delete(request, pk):
    temp = Articles.objects.get(pk=pk)
    temp.delete()
    return redirect('articles:main',1)