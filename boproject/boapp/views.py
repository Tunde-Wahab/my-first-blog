from django.shortcuts import render
from django.http import HttpResponse
from boapp.models import Dupee
from django.db.models.functions import ExtractMonth
from django.db.models import F,Count
def current_datetime(request):
   cret=Dupee.objects.create(name="Kemi")
   cret.save()
   
      
   dp=ExtractMonth(Dupee.mydate)
   pal=Dupee.objects.annotate(tm=Count(F('name')))

   pe= Dupee.objects.filter(name="kemi")
   return render(request,'index.html',{"pe":pe})
#   return render(request,'index.html',{"pal":pal})   
def test(request):
    gre=Dupee.objects.create(name="Wale")

    pet= Dupee.objects.filter(pk=2)
    return render(request,'dex.html',{"pet":pet})
# Create your views here.
