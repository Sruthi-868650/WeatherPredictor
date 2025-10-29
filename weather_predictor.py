import tkinter as tk
from tkinter import ttk
import random

def predict_weather(temperature, humidity, pressure):
    try:
        temperature = float(temperature)
        humidity = float(humidity)
        pressure = float(pressure)
    except ValueError:
        return "Invalid input"

    if temperature > 30 and humidity < 50:
        return "Sunny"
    elif pressure < 1000:
        return "Stormy"
    elif humidity > 80:
        return "Rainy"
    else:
        return random.choice(["Cloudy", "Windy", "Foggy"])  

sample_data = [
    {"temperature": 35, "humidity": 45, "pressure": 1012},
    {"temperature": 28, "humidity": 85, "pressure": 998},
    {"temperature": 22, "humidity": 60, "pressure": 1005},
    {"temperature": 40, "humidity": 20, "pressure": 990},
]

print("🧪 Console Predictions:")
for i, data in enumerate(sample_data):
    prediction = predict_weather(data["temperature"], data["humidity"], data["pressure"])
    print(f"Sample {i+1}: {data} → Predicted: {prediction}")

def create_dashboard():
    root = tk.Tk()
    root.title("Weather Prediction Dashboard ")
    root.geometry("400x300")

    ttk.Label(root, text="Temperature (°C):").pack(pady=5)
    temp_entry = ttk.Entry(root)
    temp_entry.pack()

    ttk.Label(root, text="Humidity (%):").pack(pady=5)
    humidity_entry = ttk.Entry(root)
    humidity_entry.pack()

    ttk.Label(root, text="Pressure (hPa):").pack(pady=5)
    pressure_entry = ttk.Entry(root)
    pressure_entry.pack()

    result_label = ttk.Label(root, text="", font=("Arial", 14))
    result_label.pack(pady=20)

    def on_predict():
        temp = temp_entry.get()
        humidity = humidity_entry.get()
        pressure = pressure_entry.get()
        prediction = predict_weather(temp, humidity, pressure)
        result_label.config(text=f"Predicted: {prediction}")

    ttk.Button(root, text="Predict Weather", command=on_predict).pack(pady=10)

    root.mainloop()

create_dashboard()