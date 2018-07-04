import requests
from xml.etree.ElementTree import ElementTree as etree

# r1 = requests.get("https://data.tfl.gov.uk/tfl/syndication/feeds/stations-facilities.xml?app_id=3a0c4a01&app_key=ea95c6674605181c5dde64c7bb5d883c")
# r2 = requests.get("https://tfl.gov.uk/tfl/syndication/feeds/step-free-tube-guide.xml")
# #print (r1.text)
# #r1.encoding = 'utf-8'
# with open('stations-facilities.xml', 'wb') as f:
#    f.write(r1.content)
# with open('step-free-tube-guide.xml', 'wb') as f:
#    f.write(r2.content)

tree = etree()
tree.parse("step-free-tube-guide.xml")
root = tree.getroot()
for child in root.findall('./'):
    print (child.tag, child.attrib)
#
# i = 0
# for stat in root[7].findall('station'):
#     borrar = stat.find('openingHours')
#     print(borrar)
# #    root[7].remove(borrar)
#    for child in root[7][i].iter():
#        print(stat.tag, stat.attrib)
#

