from django.shortcuts import render

def f_homepage(request):
    context = {}
    return render(request,"homepage.html",context)
