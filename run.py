import datetime
from flask import Flask, render_template
app = Flask(__name__)

@app.template_filter()
def datetimefilter(value, format='%Y/%m/%d %H:%M'):
  """Convert a datetime to a different format."""
  return value.strftime(format)
  
@app.route("/")
def home():
  return render_template('template.html', 
                          my_string="Wheeeee!",
                          my_list=[0,1,2,3,4,5],
                          current_time=datetime.datetime.now())
@app.route("/about")
def about():
  return render_template('template.html', 
                          my_string="I'm the about page",
                          my_list=[0,1,2,3,4,5],
                          current_time=datetime.datetime.now())
                          
@app.route("/contact")
def contact():
  return render_template('template.html',
                          my_string="I'm the contact page",
                          my_list=[0,1,2,3,4,5],
                          current_time=datetime.datetime.now())
                          
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)