# import requests 

# payload = {
#     "fruit": "Apple",
#     "size": "Large",
#     "color": "Red"
# }


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

# Load sensor data from file
with open("Sensors.json", "r") as file:
    sensor_data = json.load(file)

url = "http://127.0.0.1:8080/"  # Change this to your server's address

# Send POST request with sensor data
post_response = requests.post(url, json=sensor_data)

if post_response.status_code == 200:
    print("POST request successful")
    print("Server response:", post_response.json())
else:
    print("Error:", post_response.status_code)


# Send GET request to retrieve stored sensor data
get_response = requests.get(url)

if get_response.status_code == 200:
    print("GET request successful")
    print("Stored Sensor Data:")
    print(get_response.json())
else:
    print("Error:", get_response.status_code)
