from django.urls import path,include

# my views module
from post import views

urlpatterns = [
    path('', views.f_homepage, name = "url_homepage"),


    path('dashboard/', include("dashboard.urls")),
    
]