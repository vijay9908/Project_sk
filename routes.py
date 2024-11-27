from flask import render_template, Blueprint
from flask import request, jsonify

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
  return render_template('home.html', active_page='home')

@routes.route('/colleges')
def colleges():
  return render_template('colleges.html', active_page='colleges')

@routes.route('/services')
def services():
  return render_template('services.html', active_page='services')

@routes.route('/about')
def about():
  return render_template('about.html', active_page='about')

@routes.route('/test')
def test():
  return render_template('test3.html')