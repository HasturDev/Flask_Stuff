from flask import Flask
import nltk
import matplotlib
import Functions.html as funcpage
import Index.html as startpage

# add functions here for testing
def integer_thingy():
 app = Flask(__name__)

@app.route("/")
def hello():
    return startpage

@app.route("/functions")
def functions():
    return funcpage


if __name__ == '__main__':
    app.run(debug=True)