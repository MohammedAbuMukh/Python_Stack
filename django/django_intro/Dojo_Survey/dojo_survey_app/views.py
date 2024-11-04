from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'index.html')

def result(request):
    context = {
        'name_from_form': request.POST['name'],
        'location_from_form' : request.POST['location'],
        'fav_lang_from_form' : request.POST['language'],
        'comment_from_form' : request.POST['comment']
    }
    return render(request, 'result.html', context)
