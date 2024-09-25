from django.urls import path
from .views import *

app_name="myapp"

urlpatterns = [
    path("",home,name="home"),
    path("signin",signin,name="signin"),
    path("loginreal",loginreal,name="loginreal"),
    path("instructions",instructions,name="instructions"),
    path("votingPage",votingPage,name="votingPage"),
    path("about",about,name="about"),
]
