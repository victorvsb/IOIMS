
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render

def auth_login(request):
    
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    
    if request.method == 'GET':

        return render(request, 'login.html')

    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        if 'next' in request.GET:
            return HttpResponseRedirect(request.GET['next'])
        return HttpResponseRedirect('/')
    
    return render(request, 'login.html', {'error': 'Invalid credentials'})


def auth_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')