from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'hello/index.html')

def naresh(request):
    return HttpResponse("Hello Naresh!")

def greet(request, name):
    return render(request, 'hello/greetings.html', {
        'name': name.capitalize()
        })

