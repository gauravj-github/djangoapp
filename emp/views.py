from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def empp(request):
    return render(request, "emptem/homemp.html",{})