from django.shortcuts import render

from app.models import *

# Create your views here.

def Data_Team(request):
    lot=Team.objects.all()
    d={'Topics':lot}
    return render(request,'one.html',context=d)

def Data_Webpage(request):
    lto=Webpage.objects.all()
    d={'Web':lto}
    return render(request,'two.html',d)

def Data_AccessRecord(request):
    ll=AccessRecord.objects.all()
    d={'Access':ll}
    return render(request,'three.html',d)