import base64
from django.http import HttpResponse
from django.shortcuts import render, redirect
from Detection.predict import Predict

# Create your views here.


p = Predict()
def detect(request):
    if(request.method == 'POST'):
        import pdb 
        pdb.set_trace()
        img = request.FILES.get('img')
        result = p.predictHTMLDirect(img)
        request.session['var'] = str(result)
        img = request._files.get('img')
        with img.open("rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
            decoded_string = str(encoded_string, "utf-8")
        return render(request, 'index.html',{"var":str(result), "img":decoded_string})
    else:
        return render(request,'index.html',{"var":""})

def locate(request):
    va = request.session.get('var')
    return render(request, 'map.html',{"var":str(va)})