from django.http import HttpResponse
from django.shortcuts import render, redirect
from Detection.predict import Predict
# Create your views here.


p = Predict()
def detect(request):
    if(request.method == 'POST'):
        img = request.FILES.get('img')
        result = p.predictHTMLDirect(img)
        request.session['var'] = str(result)
        return render(request, 'index.html',{"var":str(result), "img":img})
    else:
        return render(request,'index.html',{"var":""})

def locate(request):
    va = request.session.get('var')
    return render(request, 'map.html',{"var":str(va)})