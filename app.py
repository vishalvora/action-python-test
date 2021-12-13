import requests

print('this msg is from python')
print('getting data')

x = requests.get('https://strapi4-dataline4.herokuapp.com/api/clinics/1')
print(x.json())
a = {'data':{
  'name':'test from github action',
  'type':'test'
}}

y = requests.post('https://strapi4-dataline4.herokuapp.com/api/clinics', data = a)
print(y)

print('data fetching completed')
