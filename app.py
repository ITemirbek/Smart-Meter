from flask import Flask
app = Flask(__name__)

from flask import render_template, request
import requests
import json
from apscheduler.schedulers.background import BackgroundScheduler

#Can be deleted: Only to check
import time

# url should be localhost of the machine
url = "http://192.168.1.84:1080/api/all/all/now"



@app.route('/')
def base():
    return render_template('main.html')
    # return render_template('hello.html')

@app.route('/home')
def home():
	# data = requests.get(url)
	# data_json =  json.loads(data.text)
	# phase_data = {}
	# data_types = ['current', 'voltage', 'power', 'cosphi', 'frequency']
	# for phase in range(3): 
	#   phase_meter = data_json['datasets'][0]['phases'][phase]
	#   phase_data['phase_{}'.format(phase)] = {}
	#   print('phase',phase)
	#   for meter in range(5):
	#     phase_data['phase_{}'.format(phase)][data_types[meter]] = phase_meter['values'][meter]['data']
	#     print(phase_meter['values'][meter]['data'])
	
	# global phase_meter
	phase_meter = [0.1, 5, 0.5, 0.86, 840] 

	phase_data = {}
	data_types = ['current', 'voltage', 'power', 'cosphi', 'frequency']

	for phase in range(3): 
	  phase_data['phase_{}'.format(phase)] = {}
	  
	  for meter in range(5):
	    phase_data['phase_{}'.format(phase)][data_types[meter]] = phase_meter[meter]

	return render_template('home.html', phase_data = phase_data)


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