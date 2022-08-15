from flask import Flask, render_template, url_for, flash, redirect 
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'a231fb8d7350a6305b4a2eef22a2d5fd' #Using secrets from python


posts = [
    {
        'author' : 'atharva',
        'title' : 'post1',
        'content' : 'This is my first entry for the blog',
        'date_posted' : 'April 28, 2013'
    },
    {
        'author' : 'siva',
        'title' : 'post2',
        'content' : 'THis is my friend siva writing on my blog website',
        'date_posted' : 'April 29, 2013'
    }
]

@app.route("/") ## This is our homepage route 
@app.route("/home") ## This is also the route pointing to the homepage 

def home():
    return render_template('home.html', posts = posts)

@app.route("/about") ## This will go to our about page 
def about():
    return render_template('about.html', title = 'About')

@app.route("/register", methods = ['GET', 'POST']) 
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form = form)

@app.route("/login")  
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Login', form = form)

if __name__ == "__main__":
    app.run(debug = True)