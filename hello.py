from flask import Flask, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_monent import Moment
app = Flask(__name__)

Bootstrap(app)
moment = Moment(app)
manager = Manager(app)

@app.route('/')
def hello_world():
	return render_template('user.html', name='world')

@app.route('/user/<name>')
def user(name):
	return render_template('user.html', name=name)

if __name__ == '__main__':
	manager.run()
