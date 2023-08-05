from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "helloUne/index.html")

def highFive(request):
    return HttpResponse("High Five✋!")

def dune(request):
    return HttpResponse("Hello Dune!!")

# def greet(request, name):
#     return HttpResponse(f"Hello, {name.capitalize()}!")

def greet(request, name):
    return render(request, "helloUne/greet.html",{
        "name":  name.capitalize()
    })