from flask import Flask, url_for, session, g, redirect, request, flash, render_template, send_from_directory
from datamodels import Unit
import datetime

flask = Flask(__name__)
flask.config.update(dict(DEBUG = True, USERNAME='admin', PASSWORD=''))
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