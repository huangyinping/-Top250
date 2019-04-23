from django.http import HttpResponse
from django.shortcuts import render
from Movie.models import Img
 

def testdb(request):
    
    list = Img.objects.all()

    return render(request,'show.html',{'list':list})