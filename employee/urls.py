from django.conf.urls import url
from employee.views import getEmployee

urlpatterns = [
	url('getEmployee', getEmployee)
]