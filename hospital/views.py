from django.shortcuts import render
from django.shortcuts import render,redirect
from hospital.forms import LoginForm,DepartmentsForm,DepartmentHeadForm,EmployeeForm
from hospital.models import Departments,DepartmentHead,Employees
from django.contrib import messages

from django.contrib.auth.models import User
from django.views.generic import View,CreateView,FormView,TemplateView,ListView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout


# Create your views here.


class LoginView(FormView):
    form_class=LoginForm
    template_name="login.html"


    def post(self,request,*args,**kw):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            user=authenticate(request,username=uname,password=pwd)
            if user:
                login(request,user)
                print("success")
                return redirect("base")
            else:
                return render(request,self.template_name,{"form":form})


class DepartmentcreateView(CreateView):
    model=Departments
    form_class=DepartmentsForm
    template_name="home.html"
    success_url=reverse_lazy("list")

    def form_valid(self, form):
        form.instance.user=self.request.user
        messages.success(self.request,"dept created")
        return super().form_valid(form)


class DeptlistView(ListView):
    model=Departments
    context_object_name="depts"
    template_name="deptlist.html"


class DeptdeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Departments.objects.filter(id=id).delete()
        messages.success(request,"removed successfully")
        return redirect("list")


class DepteditView(UpdateView):

    model=Departments
    form_class=DepartmentsForm
    template_name="deptupdate.html"
    pk_url_kwarg:str="id"
    success_url=reverse_lazy("list")

    def form_valid(self, form):
        messages.success(self.request,"department changed")
        return super().form_valid(form)



class DeptheadcreateView(CreateView):
    model=DepartmentHead
    form_class=DepartmentHeadForm
    template_name="headadd.html"
    success_url=reverse_lazy("headlist")

    def form_valid(self, form):
        form.instance.user=self.request.user
        messages.success(self.request,"dept head created")
        return super().form_valid(form)


class DeptheadlistView(ListView):
    model=DepartmentHead
    context_object_name="heads"
    template_name="headlist.html"


class DeptheaddeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        DepartmentHead.objects.filter(id=id).delete()
        messages.success(request,"removed successfully")
        return redirect("headlist")



class DeptheadeditView(UpdateView):

    model=DepartmentHead
    form_class=DepartmentHeadForm
    template_name="deptupdate.html"
    pk_url_kwarg:str="id"
    success_url=reverse_lazy("headlist")

    def form_valid(self, form):
        messages.success(self.request,"department changed")
        return super().form_valid(form)


class EmpcreateView(CreateView):
    model=Employees
    form_class=EmployeeForm
    template_name="empadd.html"
    success_url=reverse_lazy("emplist")

    def form_valid(self, form):
        form.instance.user=self.request.user
        messages.success(self.request," employee created")
        return super().form_valid(form)



class EmplistView(ListView):
    model=Employees
    context_object_name="emps"
    template_name="emplist.html"


class EmpdeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("id")
        Employees.objects.filter(id=id).delete()
        messages.success(request,"removed successfully")
        return redirect("emplist")



class EmpeditView(UpdateView):

    model=Employees
    form_class=EmployeeForm
    template_name="empupdate.html"
    pk_url_kwarg:str="id"
    success_url=reverse_lazy("emplist")

    def form_valid(self, form):
        messages.success(self.request,"emp updated")
        return super().form_valid(form)

class IndexView(TemplateView):
    template_name="base.html"



def signout(request,*args,**kw):
    logout(request)
    return redirect("signin")






