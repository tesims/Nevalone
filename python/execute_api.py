import requests

url = 'http://localhost:5000/api/chat'
data = {'user_input': 'Hello'}

response = requests.post(url, json=data)

print(response.status_code)  # Print the response status code
print(response.json())  # Print the response content as JSON