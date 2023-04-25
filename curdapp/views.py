from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import *
# Create your views here.
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def employee_list(request):
    dic_emply = {
        'emp_list': Employee.objects.all()
    }
    return render(request, 'employee_list.html', dic_emply)


def home(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = EmployeeForm()
        else:
            emp = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=emp)
        return render(request, 'employee_form.html', {'form': form})
    else:
        if id==0:
             form = EmployeeForm(request.POST)
        else:
            emp = Employee.objects.get(pk=id)
            form=EmployeeForm(request.POST,instance=emp) 
        if form.is_valid():
            form.save()
        return redirect('employee_list')
def emplyee_del(request,id):
    emp=Employee.objects.get(pk=id)
    emp.delete()
    return redirect('employee_list')