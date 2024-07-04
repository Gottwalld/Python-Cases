from pprint import pprint 
import json

file_name = r'C:\Users\skiri\OneDrive\Desktop\Python Cases\JSON\Human Groups\group_people.json'
check_year = 1977
with open(file_name) as file:
    group_people = json.load(file)

Female_dict = {}

for i in group_people:
    Female_dict[i['id_group']] = [j['name'] for j in i['people'] if j['gender'] == 'Female' and j['year'] > 1977]

Femki = sorted(Female_dict.items(), key = lambda x: -len(x[1]))
pprint(f'Самая многочисленная группа женщин: № {Femki[0][0]}, количество женщин после {check_year} года ={len(Femki[0][1])}, состав группы : {Femki[0][1]}')