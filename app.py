from flask import Flask
app = Flask(__name__)

from flask import render_template

@app.route('/')
def base():
    return render_template('main.html')
    # return render_template('hello.html')

data = {'current': 1.2, 'voltage':220}
# Current time demonstration by taking data from server
@app.route('/home')
def home():
    for i in range(14):
        data['current'] = data['current'] +i
    return render_template('home.html', data = data)

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