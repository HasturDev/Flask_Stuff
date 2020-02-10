from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def template_test():
    return render_template('Bootstrappin.html')

url = 'Bootstrappin.html'
User_data = {'somekey':'somedata'}

if __name__ == '__main__':
    app.run(debug=True)