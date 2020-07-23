from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from wtforms import Form, TextField, PasswordField, validators

app = Flask(__name__, template_folder='templetes')
Bootstrap(app)

class LoginForm(Form):
    username = TextField('Username', [validators.Email('Please Enter Valid Email')])
    password = PasswordField('Password', [validators.Length(min=6, max=15, message='Please Enter Password between 6 to 15 Characters')])

@app.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate():
            return 'Form Submitted!'
        else:
            return render_template('index.html', form=form)
    elif request.method == 'GET':
        return render_template('index.html', form=form)