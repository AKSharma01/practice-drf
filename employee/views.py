from django.shortcuts import render
from django.http import JsonResponse
from response import response
from employee.models import Employee
import json

# Create your views here.
def getEmployee(request):
	employee = []
	employeeObject = None
	status = 200
	if(request.method.lower() == "get"):
		print("get method")
		employeeObject = Employee.objects.all()
		for o in employeeObject:
			employee.append({
				"id": o.id,
				"name": o.name,
				"age": o.age,
				"address": o.address
			})
	elif (request.method.lower() == "post"):
		print("post method")
		data = json.loads(request.body)
		employee = Employee(name=data["name"], age=data["age"], address=data["address"])
		employee.save()
		employee = [{
			"id": employee.id,
			"name": employee.name,
			"age": employee.age,
			"address": employee.address
		}]
		status = 201
	else:
		print("don't know what's going on", request.method)
	return response.success(data=list(employee), status=status, hint=None)
