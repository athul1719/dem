from django.http import HttpResponse
from django.shortcuts import render
from .models import destination
from .models import names
# Create your views here.

def home(request):
   obj=destination.objects.all()
   abj=names.objects.all()
   return render(request,'about.html',{'result':obj,'abjj':abj})

def about(request):
    return render(request,'about.html',{})

def contact(request):
    return render(request,'contact.html',{})

def news(request):
    return render(request,'news.html',{})

