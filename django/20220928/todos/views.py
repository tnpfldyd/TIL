from datetime import date
from django.shortcuts import render,redirect
from .models import Todo
# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos,
    }
    return render(request, 'todos/index.html', context)

def create(request):
    content = request.GET
    print(content['deadline'])
    if content['priority'] == 'Open this select menu' and content['deadline'] == '':
        Todo.objects.create(content=content['content'])
    elif content['priority'] == 'Open this select menu':
        Todo.objects.create(content=content['content'], deadline=content['deadline'])
    elif content['deadline'] == '':
        Todo.objects.create(content=content['content'], priority=content['priority'])
    else:
        Todo.objects.create(content=content['content'], priority=content['priority'], deadline=content['deadline'])
    return redirect('todos:index')

def delete(request, todo_pk):
    todo = Todo.objects.get(pk = todo_pk)
    todo.delete()
    return redirect('todos:index')

def update(request, todo_pk):
    todo = Todo.objects.get(pk = todo_pk)
    if todo.completed == True:
        todo.completed = False
    else:
        todo.completed = True
    todo.save()
    return redirect('todos:index')