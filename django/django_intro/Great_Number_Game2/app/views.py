from django.shortcuts import render, redirect
import random

def index(request):
    if 'rand_num' not in request.session:
        request.session['rand_num'] = random.randint(1, 100)
        request.session['attempts'] = 0  

    print(request.session['rand_num']) 
    context = {
        'message': request.session.get('message', ''),
        'attempts': request.session.get('attempts', 0),
    }
    return render(request, "index.html", context)

def play(request):
    guess = int(request.POST['guess'])
    rand_num = request.session['rand_num']

   
    request.session['attempts'] += 1

   
    if guess > rand_num:
        request.session['message'] = "Too High"
    elif guess < rand_num:
        request.session['message'] = "Too Low"
    else:
        request.session['message'] = f"Correct! {guess} was the number"
       
        request.session['rand_num'] = random.randint(1, 100)
        request.session['attempts'] = 0 

    return redirect('/')
