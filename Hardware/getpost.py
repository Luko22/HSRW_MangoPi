import requests 

response = requests.get("http://127.0.0.42:8080/").json()#['data']
a=response
email= a[0]['email']
print(email)

# http://127.0.0.42:8080/

# sensor = {"velocity":"40", "Temperature": "15", "Humidity": "20"}

# upLoad= requests.post("https://httpbin.org/post", data=sensor)


# downLoad= requests.get("https://httpbin.org/get").json()

# print(downLoad['headers']['Accept-Encoding'])