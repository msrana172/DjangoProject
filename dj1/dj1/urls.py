
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index),
    path('index1/',views.index1),
    path('info/',views.methodinfo),
    path('ssession/',views.setSession),
    path('gsession/',views.getSession),
]
