from flask import Flask
from flask import jsonify

from time import sleep

app = Flask('app')

@app.route('/health-check')
def healt_check():
  return jsonify(message="ok")

@app.route('/start')
def start():
  sleep(0.02)
  return jsonify(message='started')

@app.route('/stop')
def stop():
  sleep(0.02)
  return jsonify(message='stopped')

app.run(host='0.0.0.0', port=8080)