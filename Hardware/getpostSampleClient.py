# import requests 

# sensor = {"Temperature": "15", 
#           "Speed": "20"}

# response = requests.get("http://127.0.0.42:8080/Sample.Json")#, params= payload)
# print(response)
# print(response.content)

# answer = requests.post("http://127.0.0.42:8080/Post.json", data= sensor)#, params= payload)
# print(answer)
# print(answer.content)
###########################################################
import requests
import json

# Load multiple sensor data readings from file
with open("Sensors.json", "r") as file:
    sensor_data_list = json.load(file)

url = "http://127.0.0.1:8080/"  # Change this to your server's address

# Send multiple POST requests with sensor data readings
for sensor_data in sensor_data_list:
    post_response = requests.post(url, json=sensor_data)
    if post_response.status_code == 200:
        print("POST request successful")
        print("Server response:", post_response.json())
    else:
        print("Error:", post_response.status_code)

# Send a GET request to retrieve all stored sensor data
get_response = requests.get(url)

if get_response.status_code == 200:
    print("GET request successful")
    stored_sensor_data = get_response.json()
    print(stored_sensor_data)
else:
    print("Error:", get_response.status_code)

