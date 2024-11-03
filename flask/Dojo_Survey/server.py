from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/result', methods=['POST'])
def result():
    form_data = request.form
    print(form_data) 
    return render_template("result.html", data=form_data)

if __name__ == "__main__":
    app.run(debug=True)
