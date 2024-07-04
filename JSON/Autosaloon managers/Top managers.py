import json
from pprint import pprint
with open(r'c:\Users\skiri\OneDrive\Desktop\manager_sales.json') as file:
    json_data = json.load(file)

dict_autosalon = {}

for i in json_data:
    dict_autosalon.setdefault(i['manager']['last_name'], [i['manager']['first_name'], sum([car['price'] for car in i['cars']])])

autosalon_sorted = sorted(dict_autosalon.items(), key = lambda x: -x[1][1])
print(f'{autosalon_sorted[0][1][0]} {autosalon_sorted[0][0]} {autosalon_sorted[0][1][1]}')
print(f'{autosalon_sorted[1][1][0]} {autosalon_sorted[1][0]} {autosalon_sorted[1][1][1]}')
print(f'{autosalon_sorted[2][1][0]} {autosalon_sorted[2][0]} {autosalon_sorted[2][1][1]}')