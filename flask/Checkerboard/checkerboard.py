from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def display():
    return render_template('index.html')


@app.route('/<int:x>/<int:y>')
def changeSquares(x, y):
    return render_template("change_squares.html", rows=x, columns=y)


# @app.route('/<int:x>')
# def display_num(x):
#     return render_template('index.html', times=x) 

# @app.route('/<int:x>/<int:y>')
# def display_col_row(x,y):
#     return render_template('change_squares.html', x , y) 

# @app.route('/play/<int:x>/<color>')
# def take_color(x,color):
#     return render_template('play.html', times=x, color=color)

   

if __name__=="__main__":    
    app.run(debug=True) 