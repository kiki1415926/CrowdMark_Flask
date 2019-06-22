from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from students import CMStudent

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

assignments = [
    {
        'title': 'calculus-7cdb',
        'content': ['crowdmark-exam-fd969', 'test-2-crowdmark-5e727', 'tutorial-7-fiscal'],
        'num_content': 3
    },
    {
        'title': 'linear-algebra-fall-2017',
        'content': ['tutorial-8-money-and-banking', 'tutorial-6-as-ad'],
        'num_content': 2
    }
]

student = CMStudent()
table = []

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        student.username = form.email.data
        student.password = form.password.data
        bol = student.signIn()
        if bol:
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', table=student.table)

if __name__ == '__main__':
    app.run(debug=True)
