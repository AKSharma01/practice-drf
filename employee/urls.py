from django.urls import include, path

from .views import getEmployee

urlpatterns = [
	path('getEmployee', getEmployee, name='get_employee'),
]
