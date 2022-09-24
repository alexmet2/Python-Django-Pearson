from django.shortcuts import render
from django.http import HttpResponse


def index(response):
	return render(response,"main/Homepage.html")

def Calculator(request):
	return render (request, "main/Calculator.html",{})
	
def add(request):
	Number_X = int(request.POST['NumberX'])
	Number_Y = int(request.POST['NumberY'])
	result = Number_X + Number_Y
	return render (request, "main/add.html",{'result':result})