from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from webapp.forms import TodoForm
from  webapp.models import Todo
from django.http import HttpResponseRedirect, HttpResponseNotFound, Http404

def index_view(request):
    context = {
        'todos': Todo.objects.all()
    }
    return render(request, 'index.html', context)

def todo_view(request, pk):
    # try:
    #     article = Article.objects.get(pk=pk)
    # except Article.DoesNotExist:
    #     # return HttpResponseNotFound('Article not found')
    #     raise Http404('Article not found')
    todo = get_object_or_404(Todo, pk=pk)
    return render(request, 'todo_view.html', {'todo': todo})



def todo_create_view(request):

    if request.method == 'GET':
        form = TodoForm()
        return render(request, 'create_todo.html', {'form': form})
    elif request.method == 'POST':
        form = TodoForm(data= request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            task = form.cleaned_data.get('task')
            todo = Todo.objects.create(title=title, task=task)
            return redirect('todo_view', pk=todo.id)
        else:
            return render(request, 'create_todo.html', {'form': form})


def todo_update_view(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'GET':
        form = TodoForm(initial={'title': todo.todo, 'task': todo.task})
        return render(request, 'update_todo.html', {'todo': todo, 'form': form})
    elif request.method == 'POST':
        form = TodoForm(data=request.POST)
        if form.is_valid():
            todo.title = form.cleaned_data.get('title')
            todo.task = form.cleaned_data.get('task')
            todo.save()
            return redirect('todo_view', pk=todo.id)
        else:
            return render(request, 'update_todo.html', {'todo': todo, 'form': form})



def todo_delete_view(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == "GET":
        return render(request, 'delete_todo.html', {'todo': todo})
    elif request.method == "POST":
        todo.delete()
        return redirect('todo_list')