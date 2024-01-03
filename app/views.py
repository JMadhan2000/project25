from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.models import *
def htmlforms(request):
    if request.method=='POST':
        Tn=request.POST['tn']
        TP=Topic.objects.get_or_create(Topic_name=Tn)[0]
        TP.save()
        return HttpResponse('Topic name created')
    return render(request,'htmlforms.html')



def htmlforms2(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    if request.method=='POST':
        Tn=request.POST['Tn']
        tn=request.POST['tn']
        tu=request.POST['te']
        te=request.POST['te']
        TOB=Topic.objects.get(Topic_name=Tn)
        TO=WebPage.objects.get_or_create(topic_name=TOB,name=tn,url=tu,email=te)[0]
        TO.save()
        QLWO=WebPage.objects.all()
        d1={'topics':QLWO}
        return render(request,'display.html',d1)
    return render(request,'htmlforms2.html',d)


def WebPage_multiples(request):
    
    return render(request,'WebPage_multiples.html')