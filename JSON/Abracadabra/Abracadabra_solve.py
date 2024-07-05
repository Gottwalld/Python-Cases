# Цифры, знаки препинания и пункцтуацию нужно игнорировать
import json
from pprint import pprint
from string import punctuation
punctuation = punctuation + ' '

json_file_name = r"C:\Users\skiri\OneDrive\Desktop\Python Cases\JSON\Abracadabra\Alphabet.json"
text_file = r"C:\Users\skiri\OneDrive\Desktop\Python Cases\JSON\Abracadabra\Abracadabra__1_.txt"

with open(json_file_name, 'r') as file1, open(text_file, 'r') as file2:
    json_file_code = json.load(file1)
    text = file2.read().split('\n')
    
# pprint(json_file_code)
# print(text)
# print(punctuation)

Decoded_text = [[json_file_code[letter] if letter not in punctuation else letter for letter in line ]  for line in text]
# print(Decoded_text)

for i in Decoded_text:
    print(''.join(i))