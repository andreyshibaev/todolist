from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .forms import TodoForm
from .models import Todo


@login_required
def currenttodo(request):
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'maketodo/listtodo.html', {'todos': todos})


@login_required
def completetodos(request):
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=False).order_by('datecompleted')
    return render(request, 'maketodo/completedtodos.html', {'todos': todos})



def home(request):
    return render(request, 'home.html')


@login_required
def createtodo(request):
    if request.method == 'GET':
        return render(request, 'maketodo/createtodo.html', {'form': TodoForm()})
    else:
        try:
            form = TodoForm(request.POST)
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('maketodo:currenttodo')
        except ValueError:
            return render(request, 'maketodo/createtodo.html', {'form': TodoForm(), 'error': 'Failed request to server'})


@login_required
def viewtodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'GET':
        form = TodoForm(instance=todo)
        return render(request, 'maketodo/viewtodo.html', {'todo': todo, 'form': form})
    else:
        try:
            form = TodoForm(request.POST, instance=todo)
            form.save()
            return redirect('maketodo:currenttodo')
        except ValueError:
            return render(request, 'maketodo/viewtodo.html', {'todo': todo, 'form': form, 'error': 'Bad value'})


@login_required
def completetodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.datecompleted = timezone.now()
        todo.save()
        return redirect('maketodo:currenttodo')


@login_required
def deletetodo(request, todo_pk):
    todo = get_object_or_404(Todo, pk=todo_pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('maketodo:currenttodo')
