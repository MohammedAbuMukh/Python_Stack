from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"

@app.route('/Champion')
def champion():
    return "Champion!"

@app.route('/say/<username>')
def say_flask(username):
    print(username)
    return "Hi " + username + "!"

@app.route('/repeat/<int:count>/<word>')
def repeat_word(count, word):
    return (word + ' ') * count

@app.errorhandler(404)
def page_not_found(e):
    return "Sorry! No response. Try again.", 404
   
    
if __name__=="__main__":
    app.run(debug=True)

