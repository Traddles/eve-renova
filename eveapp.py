from eve import Eve
from flask import Flask, url_for, session, g, redirect, request, flash, render_template, send_from_directory, jsonify
from flask.ext.mongoengine import MongoEngine, MongoEngineSessionInterface
import datetime, sys

# APP
#######
# Eve
app = Eve()
# Flask
flask = Flask(__name__)

# DATABASE
############
# Database config
flask.config["MONGODB_SETTINGS"] = {'DB': "eve"}
#flask.config["MONGODB_DB"] = "flaskie"
flask.config["SECRET_KEY"] = "M3\xbd\xe4\xa5 g\x13\x10\x98\xa8\xb3@\xb5z\xfd\x02J\x90\xfd\x9cC\x87\x11"
# Database connection
engine = MongoEngine(flask)
#client = engine.connection
#db = client.eve

# Model
class Unit(engine.DynamicDocument):
	created_at = engine.DateTimeField(default=datetime.datetime.now, required=True, db_field ="_created")
	updated_at = engine.DateTimeField(default=datetime.datetime.now, required=True, db_field ="_updated")
	#allowed_fields = engine.DictField(required=False, db_field ="_fields")
	#field_types = engine.DictField(required=False, db_field ="_types")
	name = engine.StringField(max_length=30, required=True)
	state = engine.StringField(max_length=30, required=False)
	def __unicode__(self):
		return self.name

def get_units(state):
	units = Unit.objects
	res = {}
	if state and state not in ["on", "off"]:
		return error_handling('03')
	for e in units:
		if not state:
			res[str(e.id)] = {'name': e.name, 'state': e.state}
		elif e.state == state:
			res[str(e.id)] = {'name': e.name, 'state': e.state}
	return res

def get_unit(name):
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
	print e
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
	app.run(debug=True, port=5111)