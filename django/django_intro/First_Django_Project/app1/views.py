from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return redirect("/blogs")
    # return HttpResponse("this is the equivalent of @app.route('/')!")

def blogs(request):
    return HttpResponse("placeholder to display a new form to create a new blog with a method named index")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect('/')

def show(request, number):
    return HttpResponse(f"placeholder to display blog number: {number}")

def edit(request, number):
    return HttpResponse(f"placeholder to edit blog {number}")

def destroy(request, number):
    return redirect("/blogs")