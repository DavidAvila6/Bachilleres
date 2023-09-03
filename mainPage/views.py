from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def principalHub(request):
    return render(request, 'hub.html')

def about(request):
    return render(request, 'about.html')
