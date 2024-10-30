from flask import Flask, render_template, request, redirect , session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/users', methods=['POST'])
def create_user():
        print("Got Post Info")
        print(request.form)
        # name_from_form = request.form['name']
        # email_from_form = request.form['email']
        # return render_template("show.html", name_on_template=name_from_form, email_on_template=email_from_form)
        # name = request.form['name']
        # email = request.form['email']
        # return redirect("/show")    
        
         # Here we add two properties to session to store the name and email
        session['username'] = request.form['name']
        session['useremail'] = request.form['email']
        return redirect('/show')
    

@app.route("/show")
def show_user():
    print("Showing the User Info From the Form")
    # return render_template('show.html', name_on_template=session['username'], email_on_template=session['useremail'])
    return render_template('show.html')
        


if __name__ == "__main__":
    app.run(debug=True)
