from django.shortcuts import render

def f_homepage(request):
    context = {}
    return render(request,"homeFolder/homepage.html",context)
