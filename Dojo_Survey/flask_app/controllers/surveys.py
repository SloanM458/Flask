from flask_app import app
from flask import render_template, request, redirect, session



@app.route("/") #First page
def initial():
    return render_template("index.html")


@app.route("/process", methods = ["POST"]) #user has filled out form and is submitting it
def process():
    session["form_data"]= request.form
    return redirect("/result")



#get = view,only needed one post route 
@app.route("/result") #Displays user info
def result():
    if "client_name" not in session:
        print("Not logged in- going back to root route")
        return redirect("/")
    print("Now in welcome page")
    # print(request.form)
    # client_name = session["client_name"]
    return render_template("result.html")

