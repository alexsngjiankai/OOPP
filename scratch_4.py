from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('homepage.html')

@app.route("/profile")
def profile():
    return render_template(('profile.html'))

@app.route("/contacthelp")
def contacthelp():
    return render_template('contacthelp.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == "__main__":
     app.run(debug=True)
