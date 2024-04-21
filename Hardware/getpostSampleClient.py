import requests
import json

# Load multiple sensor data readings from file
with open("Sensors.json", "r") as file:
    sensor_data_list = json.load(file)

url = "http://127.0.0.1:8080/"  # Change this to your server's address

post_response = requests.post(url, json=sensor_data_list)
if post_response.status_code == 200:
    print("POST request successful")
    print("Server response:", post_response.json())
else:
    print("Error:", post_response.status_code)

