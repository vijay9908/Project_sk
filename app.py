from flask import Flask, render_template, Blueprint
from flask import request, jsonify
# from routes import routes

app = Flask(__name__)
# app.register_blueprint(routes)
app.config['TEMPLATES_AUTO_RELOAD'] = True

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

@app.route('/test1')
def test1():
  return render_template('test.html')

@app.route('/test2')
def test2():
  return render_template('test2.html')

@app.route('/test3')
def test3():
  return render_template('test3.html')

if __name__ == '__main__':
  app.run(debug=True)