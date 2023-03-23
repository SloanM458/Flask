from flask import Flask

app = Flask(__name__)
@app.route('/hi')
def hello():
    return"Hello from Flask!"

@app.route('/blog/<id>/<name>')  #Path variables are enclosed in <>
def view_blog(id, name):        #if i use an identifier, i MUST include it in (parameter)
    return "This is blog" + id 

    return f"This is blog {id} by {name}" #WE CAN ALSO USE F STRING INSTEAD OF THE + METHOD

if __name__ == "__main__":
    app.run(debug = True)