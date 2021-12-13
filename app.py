import requests

print('this msg is from python')
print('getting data')

x = requests.get('https://strapi4-dataline4.herokuapp.com/api/clinics/1')
print(x.json())
a = {'data':{
  'name':'test app',
  'store_id':'500'
}}

y = requests.post('https://strapi4-dataline4.herokuapp.com/api/patients', json = a)
print(y)
print(y.json())

print('data fetching completed')
