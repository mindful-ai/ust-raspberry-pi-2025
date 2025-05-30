from flask import Flask, render_template, redirect, url_for
from bmp_sensor import get_sensor_data
from gpio_control import toggle_led, get_led_status, is_button_pressed

app = Flask(__name__)

@app.route('/')
def index():
    data = get_sensor_data()
    return render_template('index.html', data=data)

@app.route('/led', methods=['GET', 'POST'])
def led():
    toggle_led()
    return redirect(url_for('led_status'))

@app.route('/led/status')
def led_status():
    status = get_led_status()
    return render_template('led.html', led_on=status)

@app.route('/button')
def button_status():
    status = is_button_pressed()
    return render_template('button.html', pressed=status)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
