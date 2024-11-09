from flask import Flask, render_template, request, session, redirect
import random

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Route for the game start
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session['name'] = request.form['name']
        session['random_number'] = random.randint(1, 100)
        session['attempts'] = 0
        session['feedback'] = None
        session['background'] = 'white'
    return render_template('index.html')

# Route for guessing
@app.route('/guess', methods=['POST'])
def guess():
    user_guess = int(request.form['guess'])
    session['attempts'] += 1
    random_number = session['random_number']
    difference = user_guess - random_number

    if difference == 0:
        session['feedback'] = 'Correct!'
        session['background'] = 'green'
    elif abs(difference) <= 10:
        session['feedback'] = 'Lil bit high' if difference > 0 else 'Lil bit low'
    elif abs(difference) <= 20:
        session['feedback'] = 'Bit big number' if difference > 0 else 'Bit low number'
    else:
        session['feedback'] = 'Too high!' if difference > 0 else 'Too low!'

    if session['attempts'] >= 10 and session['feedback'] != 'Correct!':
        session['feedback'] = 'You Lose!'
        session['background'] = 'red'

    return redirect('/')

# Route to clear the session
@app.route('/restart')
def restart():
    session.clear()
    return redirect('/')

# Route for highscore
@app.route('/highscore')
def highscore():
    highscore_data = session.get('highscore', [])
    return render_template('highscore.html', highscore=highscore_data)

@app.route('/save_score', methods=['POST'])
def save_score():
    if session.get('feedback') == 'Correct!':
        highscore_data = session.get('highscore', [])
        highscore_data.append({'name': session['name'], 'attempts': session['attempts']})
        session['highscore'] = sorted(highscore_data, key=lambda k: k['attempts'])
    return redirect('/highscore')

if __name__ == "__main__":
    app.run(debug=True)