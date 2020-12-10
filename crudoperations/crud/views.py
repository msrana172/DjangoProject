from crud.models import User
from crud.forms import StudentRegestration
from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegestration
from .models import User

# this function will add new item and show all items
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegestration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name = nm, email = em, password = pw)
            reg.save()
            fm = StudentRegestration()
            # fm.save()
    else:
        fm = StudentRegestration()   
    stud = User.objects.all() 
    return render(request, 'addandshow.html', {'form':fm, 'stu':stud})

# this function will perform update operation
def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk = id)
        fm = StudentRegestration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk = id)
        fm = StudentRegestration(request.POST, instance=pi)
    return render(request, 'updatestudent.html', {'form':fm})

# this function will delete
def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk = id)
        pi.delete()
        return HttpResponseRedirect('/')



