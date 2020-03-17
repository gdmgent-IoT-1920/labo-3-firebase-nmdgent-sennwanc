#import libraries
from flask import Flask, render_template, request

#flask server instantieren
app = Flask(__name__)

sense_values = {
    'value': '#000000',
    'type': 'hex'
}

@app.route('/')
def hello():
    return "Connected"

@app.route('/sensehat', methods=['GET', 'POST'])
def sensehat():
    if (request.method == 'POST'):
        sense_values['value'] = request.form['senseColor']
    return render_template('./sensehat.html', sense_values = sense_values)


#server constants
host = '192.168.0.251'
port = 8080

if __name__ == '__main__':
    app.run(host=host, port=port, debug=True)
