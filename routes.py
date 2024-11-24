from flask import render_template, Blueprint
from flask import request, jsonify
from app import app

main = Blueprint('main', __name__)

@app.route('/')
def home():
  return render_template('home.html', active_page='home')

@app.route('/colleges')
def colleges():
  return render_template('colleges.html', active_page='colleges')

@app.route('/services')
def services():
  return render_template('services.html', active_page='services')

@app.route('/about')
def about():
  return render_template('about.html', active_page='about')

@app.route('/test')
def test():
  return render_template('test3.html')

if __name__ == '__main__':
  app.run(debug=True, use_reloader=False)