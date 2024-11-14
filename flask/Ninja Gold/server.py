from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/')
def index():
    if 'gold' not in session:
        session['gold'] = 0
        session['activities'] = []
    if 'attempts' not in session:
        session['attempts'] = 0
    return render_template('index.html', gold=session['gold'], activities=session['activities'], attempts=session['attempts'])

@app.route('/process_money', methods=['POST'])
def process_money():
    building = request.form['building']
    gold_earned = 0

    if building == 'farm':
        gold_earned = random.randint(10, 30)
    elif building == 'cave':
        gold_earned = random.randint(15, 20)
    elif building == 'house':
        gold_earned = random.randint(13, 40)
    elif building == 'casino':
        gold_earned = random.randint(-50, 50)

    session['gold'] += gold_earned
    session['attempts'] += 1

    now = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    if gold_earned >= 0:
        activity = f"<p class='green'>Earned {gold_earned} golds from the {building}! ({now})</p>"
    else:
        activity = f"<p class='red'>Entered a casino and lost {abs(gold_earned)} golds... Ouch! ({now})</p>"

    session['activities'].insert(0, activity)

    return redirect('/')

@app.route('/save_score', methods=['POST'])
def save_score():
    name = request.form['name']
    if 'highscore' not in session:
        session['highscore'] = []
    session['highscore'].append({
        'name': name,
        'gold': session['gold'],
        'attempts': session['attempts']
    })
    session['highscore'] = sorted(session['highscore'], key=lambda k: (k['gold'], -k['attempts']), reverse=True)
    return redirect('/highscore')

@app.route('/highscore')
def highscore():
    return render_template('highscore.html', highscore=session.get('highscore', []))

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)