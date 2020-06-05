import requests
api = 'http://localhost:5000'

print('HTTP GET Request (text):')
# 'http://localhost:5000/get/text'
response = requests.get(api + '/get/text')
print('Response: ', response.text, '\n')

print('HTTP POST Request (text):')
response = requests.post(api + '/post/text', data = 'Post1')
print('Response: ', response.text, '\n')

print('HTTP GET Request (json):')
response = requests.get(api + '/get/json')
print('Whole Response: ' + str(response.json()))
print('"data" Property of the Response: ' +  str(response.json()["data"]), '\n')

print('HTTP POST Request (json):')
response = requests.post(api + '/post/json', json={"message": "mydata"})
print('Whole Response: ' + str(response.json()))
print('"data" Property of the Response: ' +  str(response.json()["data"]))