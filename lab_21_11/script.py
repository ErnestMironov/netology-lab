import xml.etree.ElementTree as ET
import json
import os

def xml_to_json(xml_file, json_file):
    print(os.getcwd())
    # Чтение XML файла
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Конвертация данных в словарь
    people = []
    for person in root.findall('person'):
        data = {child.tag: child.text for child in person}
        people.append(data)

    # Запись данных в JSON файл
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(people, f, ensure_ascii=False, indent=2)

# Использование функции
xml_to_json('people.xml', 'people.json')
