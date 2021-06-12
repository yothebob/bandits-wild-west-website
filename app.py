from flask import Flask, render_template, request, url_for
import random
from wtforms import Form,IntegerField ,StringField,TextAreaField, validators, SubmitField

app = Flask(__name__)
app.config['SECRET KEY'] = random.randrange(1000000,9999999)

app.static_folder = 'static'

class QuoteForm(Form):
    name= StringField('Name:',[validators.DataRequired()])
    email = StringField('Email:',[validators.DataRequired()])
    number = IntegerField('Phone Number',[validators.DataRequired()])
    description = TextAreaField('Please Describe What Product you are looking for?',[validators.DataRequired()])
    submit = SubmitField('Submit')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html',title='About Us')

@app.route('/contact/',methods=['GET','POST'])
def contact():
    form = QuoteForm(request.form)
    if request.method == "POST":
        return render_template('thanks.html', title='Thanks!')
    else:
        return render_template('contact.html',title='Contact', form=form)

if __name__ == '__main__':
    app.run()
