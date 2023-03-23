from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')

# import statements, maybe some other routes
    
@app.route('/success')
def success():
    return "success, HI!"
    

@app.route('/hello/<person>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(person):
    print(person)
    return "Hello, " + person + "!"

@app.route('/greet/<string:person>/<int:num>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def greet(person,num):
    return f"Hello, {person * num}"

# app.run(debug=True) should be the very last statement! 

# The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

