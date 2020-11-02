from django.shortcuts import render, redirect

from .forms import TaskForm
from .models import Task


def index(request):
    tasks = Task.objects.order_by('-id')[:10]
    return render(request, 'main/index.html', {'title': 'Task page', 'tasks': tasks})


def aboutus(request):
    return render(request, 'main/aboutus.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Form is not valid'


    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)
