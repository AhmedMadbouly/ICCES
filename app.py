from flask import Flask, flash, redirect, url_for, render_template, request, session, abort, jsonify
import os


app = Flask(__name__)


# app.secret_key
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'this_should_be_configured')
 


@app.route('/')
def home():
	if not session.get('logged_in'):
		return render_template('login.html')
	else:
		return render_template('home.html')
 
@app.route('/login', methods = ['POST'])
def do_admin_login():
	if request.form['password'] == 'admin' and request.form['username'] == 'admin':
		session['logged_in'] = True
	else:
		flash('Wrong password!')
	return home()



@app.route('/added', methods = ['POST'])
def added():
	if request.method == 'POST':
		if request.form['add']:
			flash("Done",'add')
			return redirect(url_for('home'))
		return redirect(url_for('home'))
	
@app.route('/logout')
def logout():
	session['logged_in'] = False
	return redirect(url_for('home'))

 
if __name__ == "__main__":
	try:
		app.jinja_env.auto_reload = True
		app.config['TEMPLATES_AUTO_RELOAD'] = True
		app.secret_key = os.urandom(12)
		app.run(debug=True, use_reloader=True)
	except Exception as e:
		print("Error")
