from django.urls import path,include

# my views module
from dashboard import views

urlpatterns = [
    path('', views.f_dashboard, name = "url_dashboard"),

    # CRUD Operations Urls
    path('creat/', views.f_createpage, name = "url_createpage"),
    path('update/', views.f_updatepage, name = "url_updatepage"),
    path('delete/', views.f_deletepage, name = "url_deletepage"),
]