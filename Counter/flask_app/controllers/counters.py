from flask_app import app
from flask import render_template, request, redirect, session



@app.route("/")
def clicking():
    if "clicking" in session:
        session["clicking"] += 1
        print('clicking exists!')
    else:
        print("clicking does NOT exist")
        session["clicking"] = 0
    return render_template("index.html")



@app.route("/destroy_session")
def destroy_session():
    session.clear()
    return redirect("/")

