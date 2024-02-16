from flask import Flask, render_template

app = Flask(__name__)

CARS = [
{
  'carid':1,
  'carmodel': 'Audi A4',
  'carbrand': 'Audi',
  'carrentaldailyprice': '₹ 10000',
  'totalavailable':'10'
},
  {
    'carid':2,
    'carmodel': 'Toyota Camry Sedan',
    'carbrand': 'Toyota',
    'carrentaldailyprice': '₹ 8000',
    'totalavailable':'10'
  },
{
  'carid':3,
  'carmodel': 'Toyota Accord',
  'carbrand': 'Toyota',
  'carrentaldailyprice': '₹ 9000',
  'totalavailable':'5'
},
{
  'carid':4,
  'carmodel': 'MERCEDES E CLASS',
  'carbrand': 'MERCEDES',
  'carrentaldailyprice': '₹ 20000',
  'totalavailable':'5'
}
]

@app.route("/")
def hello_world():
  return render_template('home.html', cars=CARS)
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
  