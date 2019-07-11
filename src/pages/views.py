from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(response, *args, **kwargs):
	#return HttpResponse("<h2>Home page</h2>")
	return render(response, 'home.html', {})

def about_view(response, *args, **kwargs):	
	#return HttpResponse("<h2>About page</h2>")
	return render(response, 'about.html', {})