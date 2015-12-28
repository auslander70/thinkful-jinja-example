from flask import Flask, render_template
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def hello_world():
  return render_template('hello_world.html')
  
if __name__ == '__main__':
  app.run(debug=True, host="0.0.0.0", port=8080)