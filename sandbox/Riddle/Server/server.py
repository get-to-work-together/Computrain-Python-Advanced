import json
from flask import Flask, jsonify
import random

from raadsels import raadsels

app = Flask(__name__)

@app.route('/')
def index():
  return "Raadsels API"

@app.route('/hello/<name>')
def say_hello(name):
  return "Hello "+ name

@app.route('/raadsel')
def get_raadsel():
    try:
        i = random.randint(0, len(raadsels) - 1)
        return jsonify(raadsels[i])
    except:
        return 'Invalid index', 400

app.run()