from django.shortcuts import render
import requests

def start(request):
    data=True
    result=None
    Countries=None
    while(data):
        try:
            result=requests.get('https://api.covid19api.com/summary')
            result1=result.json()['Global']
            Countries=result.json()['Countries']
            data=False
            print(result)
        except:
            data=True
    return render(request,'index.html', {'result1':result1,'Countries':Countries})
# Create your views here.
