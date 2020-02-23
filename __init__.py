from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect
from forms import ContactForm
import os
from Email import Email_response



app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
        TESTING=True,
        SECRET_KEY='onetwo34fif!',
        DATABASE=os.path.join(app.instance_path, 'venv.sqlite')
    )
csrf = CSRFProtect()

@app.route('/', methods=('GET', 'POST'))
def contact():
    csrf.init_app(app)
    form = ContactForm()
    if form.validate_on_submit():
        Email_data = form.user_email.data
        Name_data = form.user_name.data
        Email_response.receiver_email = Email_data
        Email_response
        return redirect('/Congratulations')
    return render_template('Bootstrappin.html', form=form)

@app.route('/Congratulations', methods=('GET', 'POST'))
def congratulations():
    return render_template('congratulations.html')

if __name__ == '__main__':
    app.run(debug=True)