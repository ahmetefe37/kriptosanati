from django.shortcuts import render,HttpResponse

def f_dashboard(request):
    context = {}
    return render(request,"dashFolder/base.html",context)

def f_createpage(request):
    context = {}
    return HttpResponse("Create Page")

def f_updatepage(request):
    context = {}
    return HttpResponse("Update Page")

def f_deletepage(request):
    context = {}
    return HttpResponse("Delete Page")