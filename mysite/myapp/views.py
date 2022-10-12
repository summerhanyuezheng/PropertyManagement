from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import pandas.io 
import json
from .models import Data

# Create your views here.
def hello(request):
    if (request.method == 'POST'):
        previous_data = Data.objects.all()
        previous_data.delete()
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
            #name = name 
            #left side is the name from models.py Data object
            #we are taking all the names from models.py
            #and storing the values into it. the values are: d['property_name']
            #dt is a Data object
            dt = Data(name=name, price=price,rent=rent,
                    emi=emi, tax=tax,exp=exp)
            #save object dt into the datbase
            dt.save()
    else:
        print('This is a get request')
    
    return render(request, 'myapp/index.html')
