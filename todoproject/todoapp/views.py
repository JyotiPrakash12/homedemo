from django.shortcuts import render
from django.http import HttpResponse
from todoapp.models import Task


def index(request):
    # return HttpResponse("Hello, world. You're at the MY TODO APP.")
    task = Task.objects.all()
    if request.method == 'POST':
        new_task = request.POST.get('text')
        if new_task != "":
            newtask = Task(description = new_task, completed = False)
            newtask.save()
    context = {
        'tasks': task,

    } 
    return render(request,'todo/index.html',context)

# Create your views here.
