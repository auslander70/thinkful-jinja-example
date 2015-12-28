from flask import Flask, render_template
from os import environ

app = Flask(__name__)

class jediname(object):
  def __init__(self, firstname, lastname):
    self.firstname = firstname
    self.lastname = lastname
    
  def JediNameConstructor(self):
    part1 = self.firstname[:2]
    part2 = self.lastname[:3]
    name = part2 + part1
    return name
    
    
@app.route("/")
@app.route("/hello")
def hello_world():
  return render_template('hello.html',
                          my_name='world')

@app.route("/hello/<name>")
def hello_name(name):
  return render_template('hello.html',
                          my_name=name)
                          
@app.route("/jedi/<firstname>/<lastname>")
def jedi(firstname,lastname):
  myJedi = jediname(firstname, lastname)
  myJediName = myJedi.JediNameConstructor()
  return render_template('hello.html',
                          my_name=myJediName)


  
if __name__ == '__main__':
  app.run(debug=True, host="0.0.0.0", port=8080)