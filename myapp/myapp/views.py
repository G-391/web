from django.shortcuts import render,redirect
from django.http import HttpResponse

def home(request):
    return render(request,"home.html")

def cal(request):
    return render(request,"cal.html")

def cer(request):
    return render(request,"cer.html")

def meekrathee(request):
    return render(request, 'meekrathee.html')

def miangkham(request):
    return render(request, 'miangkham.html')

def fishorange(request):
    return render(request, 'fishorange.html')

def Lonkembaknat(request):
    return render(request, 'Lonkembaknat.html')

def kanghetphor(request):
    return render(request, 'kanghetphor.html')