from flask import Flask
import nltk
import matplotlib

# add functions here for testing
def integer_thingy():
    for i in range(5):
        return i

app = Flask(__name__)

@app.route("/")
def hello():
    return index.html

@app.route("/functions")
def functions():
    return '<h1>Your Integers are {}</h1>'.format(integer_thingy())


if __name__ == '__main__':
    app.run(debug=True)