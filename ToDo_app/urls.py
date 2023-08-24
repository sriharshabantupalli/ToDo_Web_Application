from django.urls import path
from . import views


urlpatterns = [
    path('', views.SigninSignup, name='Signin/Signup'),
    path('home', views.home, name='home'),
    path('home/tasks', views.tasks, name='tasks'),
    path('home/tasks/UpdateTask', views.UpdateTask, name='tasks'),
    path('signup', views.handleSignup, name='handleSignup'),
    path('login', views.handleLogin, name='handleLogin'),
    path('logout', views.handleLogout, name='handleLogout'),
    path('delete', views.handleDelete, name='handleDelete'),
    path('home/textutil',views.textutil, name="textutil"),
    path('home/textutil/analyze',views.textutilAnalyze, name="textutilAnalyze"),
    path("home/IcecreamHome", views.icecreamHome, name='icecreamHome'),
    path("home/IcecreamHome/about", views.icecreamAbout, name='icecreamAbout'),
    path("home/IcecreamHome/services", views.icecreamServices, name='icecreamServices'),
    path('home/IcecreamHome/contact', views.icecreamContact, name='icecreamContact'),
    path('home/CodeX', views.CodeXhome, name='CodeXhome'),
    path('home/CodeX/CodeXcontact', views.CodeXcontact, name='CodeXcontact'),
    path('home/CodeX/CodeXabout', views.CodeXabout, name='CodeXabout'),
]
