from django.shortcuts import render, redirect
from .models import Dojo,Ninja

def index(request):
    context = {
        'dojos': Dojo.objects.all()
    }
    return render(request, 'index.html', context)

def add_dojo(request):
    if request.method == 'POST':
        Dojo.objects.create(
            name=request.POST['name'],
            city=request.POST['city'],
            state=request.POST['state']
        )
    return redirect('index')

def add_ninja(request):
    if request.method == 'POST':
        dojo = Dojo.objects.get(id=request.POST['dojo'])
        Ninja.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            dojo=dojo
        )
    return redirect('index')

def delete_dojo(request, dojo_id):
    dojo = Dojo.objects.get(id=dojo_id)
    dojo.delete()
    return redirect('index')
