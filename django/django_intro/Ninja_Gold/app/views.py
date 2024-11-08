from django.shortcuts import render, redirect
from django.utils import timezone
import random


def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
        request.session['activities'] = []
        
    context ={
            'gold' : request.session['gold'],
            'activities' : request.session['activities']
        }
        
    return render(request, 'index.html', context)
    

def process_money(request):
    if request.method == 'POST':
        location = request.POST['location']
        gold_earned = 0
        
        if location == 'farm':
            gold_earned = random.randint(10,20)
        
        elif location == 'cave':
             gold_earned = random.randint(10,20)
             
        elif location == 'house':
             gold_earned = random.randint(10,20)
             
        elif location == 'quest':
             gold_earned = random.randint(-50,50)     
        
        
        request.session['gold'] += gold_earned
        timestamp = timezone.now().strftime('%Y-%m-%d %I:%M %p')
        
        if gold_earned >=0:
            activity = f"You entered a {location} and earned {gold_earned} gold. ({timestamp})"
            request.session['activities'].append({'message': activity, 'color': 'green'})
            
        else:
            activity = f"You failed a {location} and lost {abs(gold_earned)} gold. Ouch. ({timestamp})"
            request.session['activities'].append({'message': activity, 'color': 'red'})
                
                      
        request.session.modified = True
        return redirect('/')
    
             
def reset(request):
    request.session.clear()
    return redirect('/')    