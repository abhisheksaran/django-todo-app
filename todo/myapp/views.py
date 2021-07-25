from django.shortcuts import render

# Create your views here.

def home(request):
    return HttpResponse("This is the home page, you can add your new tasks here")

def pending(request):
    return HttpResponse("Here is your pending tasks")

def done (request):
    reuturn HttpResponse("Here is your completed tasks.")
