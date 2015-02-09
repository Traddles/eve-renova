from eve import Eve
from flask import Flask, url_for, session, g, redirect, request, flash, render_template, send_from_directory
from flask.ext.mongoengine import MongoEngine, MongoEngineSessionInterface

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
client = engine.connection
db = client.eve


# MAIN
if __name__ == '__main__':
	app.run(debug=True)
    #flask.run(debug=True)
