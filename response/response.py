from django.http import JsonResponse

def success(data=None, status=200, hint=None):
	return JsonResponse({
		"data": data,
		"status": status,
		"errorMessage": hint
	}, status=status)

def failure(status, hint=None):
	return JsonResponse({
		"status": status if status else 500,
		"errorMessage": hint
	}, status=status)