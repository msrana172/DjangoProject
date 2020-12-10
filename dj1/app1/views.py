from django.shortcuts import redirect, render
from app1.forms import EmployeeForm, StudentForm
from django.http import HttpResponse
from app1.functions.functions import handle_upload_file

def setSession(request):
    request.session['sname'] = 'mahaveer'
    request.session['semail'] = 'mahaveersingh7810@gmail.com'
    return HttpResponse('Session Set')
def getSession(request):
    studentname = request.session['sname']
    studentemail = request.session['semail']
    return HttpResponse(studentname + " " +studentemail)
 
def methodinfo(request):
    return HttpResponse("Http request is : " + request.method)

def index(request):
    if request.method =='POST':
        fm = StudentForm(request.POST, request.FILES)
        if fm.is_valid():
            handle_upload_file(request.FILES['file'])
            return HttpResponse("The upload Successfully !!!")
    else:
        fm = StudentForm()
        return render(request, 'index.html', {'form':fm})        
    
    # return render(request,'index.html', {'form':fm})
def index1(request):
    if request.method == "POST":
        fm = EmployeeForm(request.POST)
        if fm.is_valid():
            try:
                return redirect('/')
            except:
                pass
    else:
        fm = EmployeeForm()
    return render(request,'index.html', {'form':fm})    
            
