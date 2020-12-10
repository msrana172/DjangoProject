from django import forms
from django.forms import fields
from app1.models import Employee

class StudentForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    file = forms.FileField()
    

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

