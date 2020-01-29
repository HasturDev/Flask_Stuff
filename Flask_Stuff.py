from flask import Flask
import nltk
import matplotlib

# add functions here for testing
def integer_thingy():


app = Flask(__name__)

@app.route("/")
def hello():
    return index.html

@app.route("/functions")
def functions():
    return Functions.html


if __name__ == '__main__':
    app.run(debug=True)