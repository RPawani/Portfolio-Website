from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home),
    path('registration', views.cand),
    path('project', views.proj),
    path('skills', views.skil),
    path('login',views.login_page),
    path('signup',views.signup)
]