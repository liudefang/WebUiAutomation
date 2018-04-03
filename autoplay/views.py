from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from autoplay.models import UserandProduct


@login_required()
def index(request):
    user = request.user
    if user.is_admin:
        pdlist = UserandProduct.objects.all()
    else:
        pdlist = UserandProduct.objects.filter(username=user)
    return render(request,'index1.html')

def comingsoon(request):
    return render(request,'comingsoon.html')

def nav(request):
    list = map(str, range(10))
    List = {'name':'mike.liu','mail':'mike.liu@jfz.com'}
    return render(request,'nav.html',{'List':List})

def verify(request,query_dict):
    '''验证用户名和密码'''
    user = authenticate(username=query_dict["username"],password=query_dict["password"])
    if user is not None:
        login(request,user)
        return "验证成功"
    else:
        return "用户名或密码错误"

def login_page(request):
    if request.method == "POST":
        return HttpResponse(verify(request,request.POST))
    return render(request,"login.html")

def _logout(request):
    logout(request)
    return render("/login")