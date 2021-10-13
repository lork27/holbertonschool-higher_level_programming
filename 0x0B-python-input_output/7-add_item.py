#!/usr/bin/python3
'''module with add_arguments function'''
import json
from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

lista = []

try:
    lista = load_from_json_file("add_item.json")
except:
    pass
for i in range(1, len(argv)):
    lista.append(argv[i])

save_to_json_file(lista, "add_item.json")
