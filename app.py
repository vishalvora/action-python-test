import requests

print('this msg is from python')
print('getting data')

x = requests.get('https://jsonplaceholder.typicode.com/todos/1')
print(x)
print('data fetching completed')

