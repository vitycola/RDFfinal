import requests
from lxml import etree as ET
import xml.etree.ElementTree as ET

parser = ET.XMLParser(encoding='utf-8')

#stations = ET.parse('datos/stations-facilities.xml',parser)
tube = ET.parse('datos/step-free-tube-guide.xml',parser)

#root = stations.getroot()

#print(root)