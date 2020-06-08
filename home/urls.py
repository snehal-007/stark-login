from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name="home"),
    path("about",views.about,name="About"),
    path("contact",views.contact,name="Contact"),
    path("signup",views.signup,name="Signup")
]