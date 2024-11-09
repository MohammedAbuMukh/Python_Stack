from flask import Flask, render_template, request, redirect, session
from random import randint

app = Flask(__name__)
app.secret_key = 'super_secret_key'  

@app.route('/')
def index():
    if "Gold" not in session:
        session["Gold"] = 0
        session["massages"] = []
    return render_template('index.html')

@app.route('/prosses_money', methods=['POST'])
def prosses():
    if request.method == 'POST':
        key_of_place = request.form['key_of_place']
        if key_of_place == "farm":
            gold_farm = randint(10, 20)
            session['Gold'] += gold_farm
            message = f'Earned {gold_farm} from the farm!'
            session["massages"].append(message)
        elif key_of_place == "cave":
            gold_cave = randint(5, 10)
            session['Gold'] += gold_cave
            message = f'Earned {gold_cave} from the cave!'
            session["massages"].append(message)
        elif key_of_place == "house":
            gold_house = randint(2, 5)
            session['Gold'] += gold_house
            message = f'Earned {gold_house} from the house!'
            session["massages"].append(message)
        elif key_of_place == "casino":
            gold_casino = randint(-50, 50)
            session["Gold"] += gold_casino
            if gold_casino > 0:
                message = f'Earned {gold_casino} from the casino!'
            else:
                message = f'Lost {abs(gold_casino)} from the casino!'
            session["massages"].append(message)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
