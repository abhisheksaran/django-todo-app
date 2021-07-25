from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo
from .forms import todoForm
# Create your views here.

def home(request):
    return render(request,"myapp/home.html")

def addTask(request):
    context={}
    #creating form object
    form = todoForm(request.POST or None)

    if form.is_valid():
        form.save()
        #messages.success(request, 'Your Mod Application has been successfully submitted!')
        #print("success!!")
        return redirect('myapp:home')

    else :
        print("some error")
        print(form.errors)

    context['form']=form
    return render(request, "myapp/addTask.html",context)
    
def pending(request):
    pendingTasks = Todo.objects.filter(status="pending")
    return render(request, "myapp/pending.html",{
        "pendingTasks":pendingTasks
    })

def done (request):
    completedTasks = Todo.objects.filter(status="done")
    return render(request,"myapp/done.html",{
        "completedTasks":completedTasks
    })

def delete(request,pk):
    task = Todo.objects.get(pk=pk)
    task.delete()
    return redirect('myapp:home')
