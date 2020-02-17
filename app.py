from flask import Flask
app = Flask(__name__)

from flask import render_template

@app.route('/')
def base():
    return render_template('main.html')
    # return render_template('hello.html')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/graph')
def graph():
    return render_template('graphs.html')
    
@app.route('/weather')
def weather():
    return render_template('weather.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/hello')
def hello():
    return render_template('hello.html')