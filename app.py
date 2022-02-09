import requests, os

print('this msg is from python')
print('getting data')
print(os.getcwd())


from os import walk

filenames = next(walk(os.getcwd()), (None, None, []))[2]
print(filenames)

for f in os.listdir():
    print(f)
    with open(f) as b:
        lines = b.readlines()
        print(lines)
# with open('/requrement.txt') as f:
#     lines = f.readlines()
#     print(lines)
    
x = requests.get('https://strapi4-dataline4.herokuapp.com/api/clinics/1')
print(x.json())
a = {'data':{
  'name':'test app',
  'store_id':'500'
}}

y = requests.post('https://strapi4-applist2.herokuapp.com/api/applists', json = a)
print(y)
print(y.json())

print('data fetching completed')
