import requests 

# response = requests.get("https://reqres.in/api/users?page=2").json()['data']
# a=response
# email= a[0]['email']
# print(email)



# sensor = {"velocity":"40", "Temperature": "15", "Humidity": "20"}

# upLoad= requests.post("https://httpbin.org/post", data=sensor)


downLoad= requests.get("https://raw.githubusercontent.com/Luko22/Luko22.github.io/main/Sample.json").json()

print(downLoad)