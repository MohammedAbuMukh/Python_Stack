from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')   # The "@" decorator associates this route with the function immediately following
def index():
    return render_template('index.html', phrase="hello", times=5)
def hello_world():
    return render_template('index.html')  # Return the string 'Hello World!' as a response

# import statements, maybe some other routes
@app.route('/success')
def success():
  return "success"

@app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name):
    print(name)
    return "Hello, " + name

@app.route('/users/<username>/<id>') # for a route '/users/____/____', two parameters in the url get passed as username and id
def show_user_profile(username, id):
        print(username)
        print(id)
        return "username: " + username + ", id: " + id

@app.route('/lists')
def render_lists():
    student_info =[
        {'name' : 'Michael', 'age' : 35},
        {'name' : 'John', 'age' : 30 },
        {'name' : 'Mark', 'age' : 25},
        {'name' : 'KB', 'age' : 27}
    ]    
    return render_template("lists.html", random_numbers= [3,1,5], students = student_info)
    
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
    

### app.run(debug=True) should be the very last statement! 
    
