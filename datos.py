import requests
from lxml import etree as ET
import xml.etree.ElementTree as ET

parser = ET.XMLParser(encoding='utf-8')

#r1 = requests.get("https://data.tfl.gov.uk/tfl/syndication/feeds/stations-facilities.xml")
r2 = requests.get("https://tfl.gov.uk/tfl/syndication/feeds/step-free-tube-guide.xml")
r = r2.text
#with open('datos/stations-facilities.xml', 'w') as f:
#    f.write(r1.text)

with open('datos/step-free-tube-guide.xml', 'w') as f1:
   f1.write(r)

stations = ET.parse('datos/stations-facilities.xml',parser)