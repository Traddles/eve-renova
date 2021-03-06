from eve import Eve
from flask import jsonify
#from flask.ext.mongoengine import MongoEngine, MongoEngineSessionInterface
import datetime, sys
from datamodels import Unit

# Config
PORT = 5111
DEBUG = True


# APP
#######
# Eve
app = Eve()

# DATABASE
############
# Brought from Unit-class in datamodels module

def get_units(state):
	units = Unit.objects
	res = {}
	# TODO: Modify to comply to other states (HARDCODING PROBLEM)
	if state and state not in ["on", "off"]:
		return error_handling('03')
	for e in units:
		if not state:
			res[str(e.id)] = {'name': e.name, 'state': e.state}
		elif e.state == state:
			res[str(e.id)] = {'name': e.name, 'state': e.state}
	return res

def get_unit(unitname):
	try:
		return Unit.objects.get(name=unitname)
	except(NameError):
		#e = sys.exc_info()[0]
   		#print e
		return None

def error_handling(type, message = ''):
	if message == '':
		if type == '03':
			message = 'Input is not valid'
		elif type == '08':
			message = "Can't find any match in database"
	return {'type': type, 'message': message}

@app.route("/get")
@app.route("/get/<string:unitname>")
def search(unitname="obama"):
	e = get_unit(unitname)
	print "Get for", unitname, "result:", e
	if(e):
		return jsonify({'name': e.name, 'state': e.state})
	return jsonify(error_handling('08'))

@app.route("/all")
@app.route("/all/<string:state>")
def get_with_state(state = None):
	return jsonify(get_units(state))

@app.route('/')
def render_entries():
    entries = Unit.objects
    return render_template('show_entries.html', entries=entries)

# MAIN
if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=DEBUG, port=PORT)
