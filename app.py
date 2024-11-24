from flask import Flask, render_template, Blueprint
from flask import request, jsonify
from routes import main

app = Flask(__name__)
app.register_blueprint(main)
app.config['TEMPLATES_AUTO_RELOAD'] = True