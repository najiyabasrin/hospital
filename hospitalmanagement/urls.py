"""hospitalmanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hospital import views
from django.urls.conf import include  
from django.conf import settings  
from django.conf.urls.static import static  

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.LoginView.as_view(),name="signin"),
    path("home",views.DepartmentcreateView.as_view(),name="home"),
    path("deptdisplay",views.DeptlistView.as_view(),name="list"),
    path("remove/<int:id>",views.DeptdeleteView.as_view(),name="dept-delete"),
    path("edit/<int:id>",views.DepteditView.as_view(),name="dept-change"),
    path("headadd",views.DeptheadcreateView.as_view(),name="headadd"),
    path("headdisplay",views.DeptheadlistView.as_view(),name="headlist"),
    path("headremove/<int:id>",views.DeptheaddeleteView.as_view(),name="head-delete"),
    path("headedit/<int:id>",views.DeptheadeditView.as_view(),name="head-change"),
    path("empadd",views.EmpcreateView.as_view(),name="empadd"),
    path("empdisplay",views.EmplistView.as_view(),name="emplist"),
    path("empremove/<int:id>",views.EmpdeleteView.as_view(),name="emp-delete"),
    path("empedit/<int:id>",views.EmpeditView.as_view(),name="emp-change"),
    path("index",views.IndexView.as_view(),name="base"),
    path("logout",views.signout,name="signout"),




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
