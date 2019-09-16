from xml.etree import ElementTree as ET

tree = ET.parse('data/test.xml')
root = tree.getroot()

# search by name and value attr
first_names = root.findall('./person[@pk="22"]/first_name')
last_names = root.findall('person[@pk="22"]/last_name')
ages = root.findall('person/[@pk="22"]/age')

for values in zip(first_names, last_names, ages):
    row = {value.tag: value.text for value in values}
    print(row)


# search by index (this -- [@pk][1] -- XPATH position => 1) and attr name
first_names = root.find('./person/age/..[@pk][1]/first_name').text
print(first_names)

last_name = root.find('./person/age/..[@pk][2]/last_name').text
print(last_name)

first_names = root.findall('./person/age/..[@pk][3]/first_name')[0].text
print(first_names)
