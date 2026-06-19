from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")
    # return HttpResponse("Hello, world. You're at the hello world index.")
    # if request.method == "POST":
    #     return HttpResponse("You must have POSTed something")
    # else:
    #     return HttpResponse(request.method)
    

