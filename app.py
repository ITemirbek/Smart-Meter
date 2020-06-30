from flask import Flask
from flask import render_template, request
import requests
import json
from flask_socketio import SocketIO, send
#Can be deleted: Only to check
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)
# url should be localhost of the machine
# url = "http://192.168.1.84:1080/api/all/all/now"



@app.route('/')
def base():
    return render_template('main.html')
    # return render_template('hello.html')

@app.route('/home')
def home():
	return render_template('home.html')

labels = [
    'JAN', 'FEB', 'MAR', 'APR',
    'MAY', 'JUN', 'JUL', 'AUG',
    'SEP', 'OCT', 'NOV', 'DEC'
]

values = [
    967.67, 1190.89, 1079.75, 1349.19,
    2328.91, 2504.28, 2873.83, 4764.87,
    4349.29, 6458.30, 9907, 16297
]

colors = [
    "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA",
    "#ABCDEF", "#DDDDDD", "#ABCABC", "#4169E1",
    "#C71585", "#FF4500", "#FEDCBA", "#46BFBD"]

@app.route('/graph')
def graph():
    return render_template('graphs.html', max=17000, labels=labels, values=values)
    
# @app.route('/weather')
# def weather():
#     return render_template('weather.html')
@app.route('/about')
def about():
     return render_template('about.html')

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



# @socketio.on('my event')
# def handle_my_custom_event(msg):
# 	# data = requests.get(url)
# 	# data_json =  json.loads(data.text)
# 	# phase_data = {}
# 	# data_types = ['current', 'voltage', 'power', 'cosphi', 'frequency']
# 	# for phase in range(3): 
# 	#   phase_meter = data_json['datasets'][0]['phases'][phase]
# 	#   phase_data['phase_{}'.format(phase)] = {}
# 	#   print('phase',phase)
# 	#   for meter in range(5):
# 	#     phase_data['phase_{}'.format(phase)][data_types[meter]] = phase_meter['values'][meter]['data']
# 	#     print(phase_meter['values'][meter]['data'])
# 	print('Message: ' + msg)
# 	phase_meter = [0.1, 5, 0.5, 0.86, 840] 

# 	phase_data = {}
# 	data_types = ['current', 'voltage', 'power', 'cosphi', 'frequency']

# 	for phase in range(3): 
# 	  phase_data['phase_{}'.format(phase)] = {}
	  
# 	  for meter in range(5):
# 	    phase_data['phase_{}'.format(phase)][data_types[meter]] = phase_meter[meter]

# 	emit('some event', phase_data, broadcast=True)

@socketio.on('message')
def handleMessage(msg):
	print('Message: ' + msg)
	send(msg, broadcast=True)

	
if __name__ == "__main__":
	# app.run()
	socketio.run(app)
	# socketio.run(app, host='0.0.0.0')