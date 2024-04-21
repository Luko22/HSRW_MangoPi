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

# sensor_data = {
#     "Temperature": "15",
#     "Speed": "20"
# }

url = "http://127.0.0.1:8080/"  # Change this to your server's address

answer = requests.post("http://127.0.0.1:8080/", json=sensor_data)

if answer.status_code == 200:
    print("Data sent successfully")
    print("Server response:", answer.json())
else:
    print("Error:", answer.status_code)


response = requests.get("http://127.0.0.1:8080/")

if response.status_code == 200:
    print("GET request successful")
    print("Response:")
    print(response.text)
else:
    print("Error:", response.status_code)