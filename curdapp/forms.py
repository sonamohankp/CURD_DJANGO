from django import forms
from .models import *

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'
        
        labels={
            'fullname':'Full Name',
            'emp_code':'Emp_Code',
            'mobile':'Mobile',
            
        }
    def __init__(self,*args,**kwargs)  :
        super(EmployeeForm,self).__init__(*args,**kwargs)
        self.fields['postion'].empty_label="select your postion"
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'login.html'