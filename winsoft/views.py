from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ntrends(request):
    return HttpResponse('forex broker')
def FXPRO(request):
    return render(request,'fxpro.html')

 def nbh(request):
     return render(request,'nbh.html')