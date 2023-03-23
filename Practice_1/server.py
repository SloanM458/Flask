from flask import Flask
# I AM USING PORT 5000 HERE AND IT WORKS GOOD!
app = Flask(__name__)
@app.route('/')
def hello():
    return"Hello World!!"

@app.route('/dojo')
def dojo():
    return"Dojo!"

@app.route('/say_hi/<string:name>')
def say_hi(name):
    print(name)
    return f"Hello {name}"


# @app.route('/hello/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
# def hello(name):
#     print(name)
#     return "Hello, " + name

@app.route('/repeat/<int:num>/<string:word>')
def repeat(num, word):
    return f"{num * word}"



if __name__ == "__main__":
    app.run(debug = True)