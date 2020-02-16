from flask import Flask
app = Flask(__name__)

from flask import render_template

@app.route('/')
def base():
    return render_template('main.html')
    # return render_template('hello.html')