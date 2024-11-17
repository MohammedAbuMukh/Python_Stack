from django.shortcuts import render, redirect, HttpResponse
from . import models
from django.contrib import messages
from .models import Show


def index(request):
    return redirect('/shows')

def shows(request):
    context = {
        'shows' : models.get_all_shows()
    }
    return render(request ,"shows.html", context)

def addShow(request):
    return render(request, "showAdd.html")

def createShow(request):
    if request.method == "POST":
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)   
            return redirect('/shows/new')
        
        else :    
            models.create_show(request.POST)
            return redirect('/shows')


    else:
        return HttpResponse("Soemthing wrong!")

def showID(request, id):
    context = {
        'show' : models.get_show_by_id(id)
    }
    return render(request, "show_id.html", context)

def deleteShow(request, id):
    models.delete_show(id)
    return redirect('/shows')

def editshow(request, id ):
    context = {
        'show' : models.get_show_by_id(id=id)
    }    
    
    return render(request, 'edit_show.html', context)

    
def update(request):
    if request.method == 'POST':
        errors = Show.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key,value in errors.items():
                messages.error(request,value)
            return redirect(f'/show/{int(request.POST["id"])}/edit')
        else:
            models.update(request.POST)
        return redirect('/shows')
    else:
        return HttpResponse("somthing wrong")   
    
   