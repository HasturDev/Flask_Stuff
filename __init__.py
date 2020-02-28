from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect
from forms import ContactForm
import os
from Email import Email_response
from db import Database


app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
        TESTING=True,
        SECRET_KEY='onetwo34fif!',
        DATABASE=os.path.join(app.instance_path, 'venv.sqlite')
    )
csrf = CSRFProtect()


@app.route('/congratulations', methods=('GET', 'POST'))
def congratulations():
    return render_template('congratulations.html')

@app.route('/', methods=('GET', 'POST'))
def contact():
    csrf.init_app(app)
    form = ContactForm()
    if form.validate_on_submit():
        Email_data = form.user_email.data
        Name_data = form.user_name.data
        Email_response(form.user_email.data)
        full_user_data = (form.user_name.data, form.user_email.data, form.user_password.data)
        Database.db_cursor.execute("INSERT INTO user VALUES (?,?,?)", full_user_data)
        for row in c.execute('SELECT * FROM user ORDER BY user_name'):
            print(row)
        return redirect('/congratulations')
    return render_template('Bootstrappin.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)

