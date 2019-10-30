from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.


def auth(request):
	if request.method == 'POST':
		usern=request.POST.get('user',None)
		passw=request.POST.get('pass',None)
		user = authenticate(username=usern,password=passw)
		if user is not None:
			login(request, user)
			return redirect('ingreso:index')
		else:
			return redirect('ingreso:ingresar')
	return render(request, 'ingreso/login.html',{})

@login_required
def index(request):
	if request.user.groups.filter(name='admin').exists():
		return render(request,'ingreso/principal.html',{})
	else:
		return render(request,'anothers/indexnope.html',{})