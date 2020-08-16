from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import TodoForm
from .models import TodoList
# Create your views here.


def index(request):

    todos = TodoList.objects.all()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TodoForm()
    return render(request, "base.html", {"form":form,"todos":todos})


def delete(request, id):

    todoD = TodoList.objects.get(id=id)
    todoD.delete()
    todos = TodoList.objects.all()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TodoForm()
    return render(request, "base.html", {"form": form, "todos": todos})
