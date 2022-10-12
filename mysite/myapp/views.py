from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import pandas.io 
import json
from .models import Data

# Create your views here.
def hello(request):
    if (request.method == 'POST'):
        file = request.FILES['file']
        df = pd.read_csv(file)
        json_records= df.reset_index().to_json(orient='records')
        data = []
        data = json.loads(json_records)
        for d in data:
            name = d['property_name']
            price = d['property_price']
            rent = d['property_rent']
            emi = d['emi']
            tax = d['tax']
            exp = d['other_exp']
    else:
        print('This is a get request')
    
    return render(request, 'myapp/index.html')
