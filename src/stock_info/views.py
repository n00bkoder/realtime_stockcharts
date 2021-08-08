from django.shortcuts import render, redirect
import requests
from .forms import StockForm
from django.core.files import File
from .tasks import get_time_series_data
from stockwatch.secrets import api_key
def search (request):
    form = StockForm(request.POST or None)
    key = api_key
    if form.is_valid():
        sym = form.cleaned_data['stock_symbol']

        with open('stock_info/temp.txt', 'w') as f:
            f.write(sym)
        with open('stock_info/temp.txt', 'r+') as f:
            f.seek(0)
            symbol = f.read()
            
            f.close
       
        return redirect('/stocks/info/')
    context = {
        'form':form,
        'key': api_key,
    }
    return render(request, 'stock_info/search.html', context)


def info (request):
    get_time_series_data.delay()
   
    return render(request, 'stock_info/index.html')



    