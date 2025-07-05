from django.shortcuts import render
from . models import Employee
# Create your views here.

def home(request):
    employees = Employee.objects.all()
    return render(request,'employees/home.html',{'employees':employees})

def employee_details(request,pk):
    employee = Employee.objects.get(pk=pk)
    return render(request,'employees/employee_details.html',{'employee':employee})
