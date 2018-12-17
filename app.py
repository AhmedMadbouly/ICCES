from flask import Flask, flash, redirect, url_for, render_template, request, session, abort, jsonify
import os


app = Flask(__name__, template_folder= "templates")


# app.secret_key
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'this_should_be_configured')


@app.route('/')
def home():
	return render_template('index.html')

@app.route('/contact', methods = ['POST'])
def contact():
	# if request.method == 'POST':
	print("OK")
	return render_template('contact.html')


if __name__ == "__main__":
	try:
		app.jinja_env.auto_reload = True
		app.config['TEMPLATES_AUTO_RELOAD'] = True
		app.secret_key = os.urandom(12)
		app.run(debug=True, use_reloader=True)
	except Exception as e:
		print("Error")
