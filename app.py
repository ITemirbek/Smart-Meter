from flask import Flask
app = Flask(__name__)

from flask import render_template, request

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

@app.route('/settings', methods = ['GET' , 'POST'])
def settings():
	if request.method == 'POST':
		values = {}
		values['Rating'] = request.form['Rating']
		values['RatedFrequency'] = request.form['RatedFrequency']
		values['Impedance'] = request.form['Impedance']
		values['RatedCurrent'] = request.form['RatedCurrent']
		values['PrimaryVoltage'] = request.form['PrimaryVoltage']
		values['SecondaryVolatage'] = request.form['SecondaryVolatage']
		# return render_template('home.html', values = values)

	return render_template('settings.html')

@app.route('/hello')
def hello():	
    return render_template('hello.html')

if __name__ == "__main__":
	app.run()