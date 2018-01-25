from django.http import HttpResponse

def index(request):
	return HttpResponse("Rango says hey there partner!<br><br><a href=\"/rango/about/\">About Rango</a>")

def about(request):
	return HttpResponse("Rango says here is the about page.<br><br><a href=\"/rango/\">Back to home page</a>")
