from flask import Flask
app = Flask(__name__)


@app.route('/')
def firstly():
    return"Hello World!"

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)