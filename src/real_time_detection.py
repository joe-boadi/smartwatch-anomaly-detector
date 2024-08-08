import random
from model_training import scaler, model

def simulate_real_time_data():
    return {
        'connection_duration': random.uniform(1, 30),
        'signal_strength': random.uniform(-80, -30),
        'data_transfer_rate': random.uniform(1, 20),
        'time_of_day': random.randint(0, 23)
    }

def classify_connection(model, scaler, sample):
    data = [[sample['connection_duration'], sample['signal_strength'], sample['data_transfer_rate'], sample['time_of_day']]]
    data = scaler.transform(data)
    return model.predict(data)[0]

def block_intrusion(sample):
    print(f"Blocking intrusion: {sample}\n")

# Example usage
for _ in range(10):
    sample = simulate_real_time_data()
    prediction = classify_connection(model, scaler, sample)
    if prediction == 1:
        block_intrusion(sample)
    else:
        print(f"Normal connection: {sample}\n")