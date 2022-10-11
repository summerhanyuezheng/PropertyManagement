from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd

# Create your views here.
def hello(request):
    if (request.method == 'POST'):
        print(request.FILES['file'])
    else:
        print('This is a get request')
    
    return render(request, 'myapp/index.html')
