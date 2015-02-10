from flask import Flask, url_for, session, g, redirect, request, flash, render_template, send_from_directory
from datamodels import Unit
import datetime

flask = Flask(__name__)

def get_by_id(entry_id):
	entry = Unit.objects(id=entry_id)
	if not entry:
		abort(401)
	return entry[0]

#@flask.route('/login', methods=['GET', 'POST'])
#def login():

#@flask.route('/logout')
#def logout():


#@flask.route('/update/<entry_id>', methods=['POST'])
#def update_entry(entry_id):

@flask.route('/')
def show_entries():
    entries = Unit.objects
    return render_template('show_entries.html', entries=entries)
    return "Smile to thworld"


if __name__ == '__main__':
	# Flask
	flask.run(host='0.0.0.0', debug=True)