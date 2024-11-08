from django.shortcuts import render, redirect, session 

def index(request):
    return render(request, 'index.html')
