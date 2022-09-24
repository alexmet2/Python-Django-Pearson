from django.urls import path

from . import views

urlpatterns=[
path('',views.index,name="Start_Menu"),
path('Calculator.html',views.Calculator,name="Calculator"),
path('add',views.add,name="add"),
]