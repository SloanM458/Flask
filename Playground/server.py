# TO WHOEVER IS GRADING- JUSTIN HELPED ME WITH SOME OF THIS, THERE MAY BE SIMILARITIES

# I AM UNSURE WHY BUT MY CODE DOESN'T SEEM TO BE WORKING. I HAVE UNINSTALLED THE PIPENV AND REINSTALLED IT AND IT STILL GIVES ME ERRORS. 
#I WILL BE SPEAKING WITH A TA TOMORROW ON ZOOM TO GET REAL TIME FEEDBACK. THANK YOU! :)

from flask import Flask, render_template
app = Flask(__name__)


# test statement->
# @app.route ('/hi')
# def hello():
#     return("Hello!")

@app.route('/play')
def level_one():
    return render_template("index.html", num=3, color = "aqua")


@app.route ('/level_two/<int:x>/<string:color>')
def level_two(x, color):
    return render_template("index.html", x = x, color = color)


@app.route ('/level_three/<int:x>/<string:color>')
def level_three(x, color):
    return render_template("index.html", x = x, color = color)


if __name__=="__main__":
    app.run(debug=True)

