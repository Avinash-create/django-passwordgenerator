from django.shortcuts import render
from django.http import HttpResponse 
import random

# Create your views here.

def home(request):
	return render(request,'generator/home.html')
def about(request):
	return render(request,'generator/about.html')

def password(request):
	character = list('abcdefghijklmnopqrstuvwxyz')

	if request.GET.get('uppercase'):
		character.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
	if request.GET.get('special'):
		character.extend(list('!@#$%^&*_'))

	length = int(request.GET.get('length'))

	thepassword = ''
	for x in range(length):
		thepassword += random.choice(character)

	return render(request,'generator/password.html', {'password':thepassword})


