import requests 

response = requests.get("https://reqres.in/api/users?page=2").json()

print(response['data'])

// email= response['data'][0]['email']

print(response['data'][0]['email'])