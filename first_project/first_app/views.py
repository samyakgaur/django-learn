from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
# This will display the stuff written here when this is called from the project/url 

#creating a function 
def index(request):
    return HttpResponse('Hello World')
