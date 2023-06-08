from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
import random
from django import template


User = get_user_model()
# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def inside_base(request):
    connections = find_connections(request)
    current_user = request.user
    return render(request, 'base.html', {'users':connections, 'current_user':current_user})

def signup(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullName')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        country = request.POST.get('country')
        gender = request.POST.get('gender')
        interests = request.POST.getlist('interests')
    
        user = User.objects.create_user(
            password=request.POST.get('password'),
            email= email,
            phone=phone,
            fullname = fullname,
            country=country,
            gender=gender,
            interests=interests  
        )
        user.save()

        return redirect('login')
    else:
        return render(request, 'signup.html',{})

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('uname')
        password = request.POST.get('pass')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)

            user.is_online = True
            user.save()

            return redirect('base')
        else:
            return HttpResponse('User does not exists')


    return render(request, 'login.html',{})



def user_logout(request):
    user = request.user
    user.is_online = False
    user.save()
    logout(request)
    return redirect('index')

@csrf_exempt
def update_status(request):
    user = request.user
    if request.method == 'POST':
        status = request.POST.get('status') 
        
        if status == 'offline':
            user.is_online = False
            messages.success(request, 'Status changed to Offline')
        elif status == 'online':
            user.is_online = True
            messages.success(request, 'Status changed to Online')
        else:
            messages.error(request, 'Invalid status value')

        user.save()
        
    return redirect('base')


import random



def find_connections(request):
    user = request.user
    user_interests = set(user.interests)
    online_users = User.objects.filter(is_online=True).exclude(pk=user.pk)
    connections = []

    for online_user in online_users:
        if set(online_user.interests) & user_interests:
            connections.append(online_user)

    if not connections:
        random_user = random.choice(online_users)
        connections.append(random_user)
    
    connections = connections[0]
    return connections
    #return render(request, 'base.html', context={'users':connections})
