from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def play():
    return render_template('index.html')

@app.route('/play/<int:x>')
def play_num(x):
    return render_template('play.html', times=x) 

@app.route('/play/<int:x>/<color>')
def take_color(x,color):
    return render_template('play.html', times=x, color=color)

   

if __name__=="__main__":    
    app.run(debug=True) 