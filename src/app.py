import random
from model_training import scaler, model
from real_time_detection import classify_connection, block_intrusion
from flask import Flask, render_template, jsonify


app = Flask(__name__)

def simulate_real_time_data():
    # Simulate real-time Bluetooth connection data
    return {
        'connection_duration': random.uniform(1, 60),
        'signal_strength': random.uniform(-90, -30),
        'data_transfer_rate': random.uniform(1, 20),
        'time_of_day': random.uniform(0, 24)
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect')
def detect():
    sample = simulate_real_time_data()
    prediction = classify_connection(model, scaler, sample)
    if prediction == 1:
        block_intrusion(sample)
        return jsonify(status="Intrusion Detected", data=sample)
    else:
        return jsonify(status="Normal Connection", data=sample)

if __name__ == '__main__':
    app.run(debug=True)

