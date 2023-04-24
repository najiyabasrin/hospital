from django import forms
from django.contrib.auth.models import User
from hospital.models import Departments,DepartmentHead,Employees




class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"user name"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))



    

class DepartmentsForm(forms.ModelForm):
    class Meta:
        model = Departments
        fields = '__all__'

        widgets={
            "deptname":forms.TextInput(attrs={"class":"form-control"}),
            "deptimage":forms.FileInput(attrs={"class":"form-control"}),
            "year":forms.DateInput(attrs={"class":"form-control"}),
            "description":forms.Textarea(attrs={"class":"form-control"}),

        }


        labels ={
             'deptname': "department Name:",
             'deptimage':"departmentimage:",
             'year':"year:",
             'description':"Description:",

        }



class DepartmentHeadForm(forms.ModelForm):
    class Meta:
        model = DepartmentHead
        fields = '__all__'

        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "empno":forms.TextInput(attrs={"class":"form-control"}),
            "age":forms.TextInput(attrs={"class":"form-control"}),

            "proimage":forms.FileInput(attrs={"class":"form-control"}),
            "prodescription":forms.Textarea(attrs={"class":"form-control"}),
            "deptname":forms.TextInput(attrs={"class":"form-control"}),


        }


        labels ={
             'name': "department head Name:",
             'empno': "employee number:",
             'age': "age:",
             'proimage':"profile image:",
             'prodescription':"profile Description:",
             'deptname': "department Name:",


             


        }


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employees
        fields = '__all__'

        widgets={
            "ename":forms.TextInput(attrs={"class":"form-control"}),
            "empno":forms.TextInput(attrs={"class":"form-control"}),
            "age":forms.TextInput(attrs={"class":"form-control"}),

            "proimage":forms.FileInput(attrs={"class":"form-control"}),
            "prodescription":forms.Textarea(attrs={"class":"form-control"}),
            "deptname":forms.TextInput(attrs={"class":"form-control"}),


        }


        labels ={
             'ename': "employee Name:",
             'empno': "employee number:",
             'age': "age:",
             'proimage':"profile image:",
             'prodescription':"profile Description:",
             'deptname': "department Name:",
        }
