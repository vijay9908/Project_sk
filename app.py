from flask import Flask, render_template
from flask import request, jsonify

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/colleges')
def colleges():
  return render_template('colleges.html')

@app.route('/services')
def services():
  return render_template('services.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/test')
def test():
  return render_template('test.html')

if __name__ == '__main__':
  app.run(debug=True, use_reloader=False)