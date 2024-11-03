from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

fruit_list = ["Strawberry", "Raspberry", "Apple"]

@app.route('/')
def index():
    return render_template('fruits.html', fruits=fruit_list)

@app.route('/checkout', methods=['POST'])
def checkout():

    name = request.form.get("name")
    student_id = request.form.get("student_id")
    fruit_counts = {fruit: int(request.form.get(fruit, 0)) for fruit in fruit_list}

    total_count = sum(fruit_counts.values())

    print(f"Charging {name} for {total_count} fruits.")

    return render_template('checkout.html', name=name, student_id=student_id,
                           fruits=fruit_counts, total_count=total_count, timestamp=datetime.now())

if __name__ == "__main__":
    app.run(debug=True)
