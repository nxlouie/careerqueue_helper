from flask import Flask, render_template
import config
import time
import requests


# Initialize Flask app with the template folder address
app = Flask(__name__, template_folder='templates')

while 1:
  time.sleep(10)
  print 'beat'
  r = requests.post('http://0.0.0.0:3000/notification')


app.secret_key = "super secret key"
if __name__ == '__main__':
  # listen on external IPs
  app.run(host=config.env['host'], port=config.env['port'], debug=True)
