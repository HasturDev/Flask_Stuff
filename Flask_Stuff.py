from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect

class MyForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])

app = Flask(__name__)
app.config.update(
        TESTING=True,
        SECRET_KEY='onetwo34fif1'
    )
csrf = CSRFProtect()

@app.route('/', methods=('GET', 'POST'))
def contact():
    csrf.init_app(app)
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/')
    return render_template('Bootstrappin.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)