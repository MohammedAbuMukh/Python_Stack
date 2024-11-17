from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *

def index(request):
    return render(request, "login.html")

def registration(request):
    if request.method=='POST':
        errors = User.objects.registration_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags='register')
            return redirect('/')
        else:
            _hash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            newUser = User.objects.create(
                firstname = request.POST['firstname'],
                lastname = request.POST['lastname'],
                birth_date=request.POST['birth_date'],
                email = request.POST['email'],
                password = _hash
            )
            newUser.save()
            request.session['user_id'] = newUser.id
            messages.success(request, "Registration successful! You can now log in.", extra_tags='success')
            return redirect('/')
    else:
        return redirect ('/')
    

def login(request):   
    if request.method == 'POST':
        errors = User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags='login')
            return redirect('/')
        else:
            log_user=User.objects.get(email=request.POST['email'])
            request.session['user_id'] = log_user.id
            return redirect('/success')

def success(request):
    if not 'user_id' in request.session:
        return redirect('/')
    context = {
        "user" : User.objects.get(id=request.session['user_id'])
    }
    return render(request, "success.html", context)

def logout(request):
    if ('user_id' in request.session):
        del request.session['user_id']
    return redirect('/')