from django.shortcuts import render, redirect
from .models import * 
def index(request):
    context ={
        'books': Book.objects.all(),
    }
    return render(request, 'add_books.html',context)
    

def add_book(request):
    if request.method == 'POST':
        Book.objects.create(
            title = request.POST['title'],
            desc  = request.POST['desc']
        )
    return redirect('/')    



def view_book(request,id):
    
    return render(request, 'view_book', context)