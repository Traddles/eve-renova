from eve import Eve
from flask import Flask, url_for, session, g, redirect, request, flash, render_template, send_from_directory, jsonify
from flask.ext.mongoengine import MongoEngine, MongoEngineSessionInterface
import datetime

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


@app.route("/get-one")
def search():
	#unit = Unit.objects.get(name="obama")
	e = Unit.objects.get(name="obama")
	if(e):
		return jsonify({'name': e.name, 'state': e.state})
	#print e.state
	return jsonify({'result': True})

# MAIN
if __name__ == '__main__':
	app.run(debug=True)
    #flask.run(debug=True)
