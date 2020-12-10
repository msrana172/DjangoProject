from django.shortcuts import redirect, render
from app1.forms import EmployeeForm
from app1.models import Employee

def emp(request):
    if request == "POST":
        fm = EmployeeForm(request.POST)
        if fm.is_valid():
            try:
                fm.save()
                return redirect('/')
            except:
                pass 
    else:
        fm = EmployeeForm()
    return render(request, 'index.html', {'form':fm})    


