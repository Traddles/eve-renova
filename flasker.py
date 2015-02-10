from flask import Flask, url_for, session, g, redirect, request, flash, render_template, send_from_directory
from datamodels import Unit
import datetime

DEBUG = True

flask = Flask(__name__)
flask.debug = DEBUG
flask.config.update(dict(USERNAME='admin', PASSWORD=''))
flask.config["SECRET_KEY"] = "M3\xbd\xe4\xa5 g\x13\x10\x98\xa8\xb3@\xb5z\xfd\x02J\x90\xfd\x9cC\x87\x11"

def get_by_id(entry_id):
	entry = Unit.objects(id=entry_id)
	if not entry:
		abort(401)
	return entry[0]

@flask.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != flask.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != flask.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@flask.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))


@flask.route('/update/<entry_id>', methods=['POST'])
def update_entry(entry_id):
	if not session.get('logged_in'):
		flash("This won't work unless you login")
		return redirect(url_for('show_entries'))
	update_object = get_by_id(entry_id)

	print "This is him:", update_object.name
	for key in request.form:
		choice = request.form[key]
		print key, choice

		if choice in update_object.allowed_fields[key]:
			print "allright"
			choice = update_object.allowed_fields[key][choice]
		update_object[key] = choice

	update_object.save()
	flash('Entry was updated')
	return redirect(url_for('show_entries'))

@flask.route('/')
def show_entries():
    entries = Unit.objects
    return render_template('show_entries.html', entries=entries)
    return "Smile to thworld"


if __name__ == '__main__':
	# Flask
	flask.run(host='0.0.0.0')