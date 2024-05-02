from django.shortcuts import render
from django.http import HttpResponse

# Simple route
def home(request):
    return render(request, "home.html")
    
