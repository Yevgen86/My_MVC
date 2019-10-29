from flask import Flask, render_template, request, redirect, url_for, make_response
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    welcomeText = "Welcome to my MVC Page!"
    currentYear = datetime.datetime.now().year
    return render_template("index.html", welcomeText=welcomeText, currentYear=currentYear)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=['GET', 'POST']) # methods for the Form on this page
def contact():
    if request.method=='GET':
       # user_name = request.cookies.get("about.html", name="user_name")
        return render_template("contact.html") # , name=user_name
    elif request.method=='POST':
        inputName = request.form.get("inputName")  # we get the data from name="inputname" from the from on this page
        inputEmail = request.form.get("inputEmail")
        messageText = request.form.get("messageText")
        print(inputName, inputEmail, messageText)  # printing data in console
        # Making cookie below
        response = make_response(render_template("contact.html"))
        response.set_cookie('user_name', inputName)
        return response

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method=='GET':
        return render_template("register.html")
    elif request.method=='POST':
        return render_template("register.html")

if __name__ == '__main__':
    app.debug=True
    app.run()
