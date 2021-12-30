from django.shortcuts import render, redirect
from Detection.predict import Predict
# Create your views here.


p = Predict()
def detect(request):
    if(request.method == 'POST'):
        img = request.FILES.get('img')
        result = p.predictHTMLDirect(img)        
        return render(request, 'index.html',{"var":str(result), "img":img})
    else:
        return render(request,'index.html',{"var":""})
