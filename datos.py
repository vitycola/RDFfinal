import requests
from xml.etree.ElementTree import ElementTree as etree
import xml.etree.ElementTree as ET

def getData():
    r1 = requests.get("https://data.tfl.gov.uk/tfl/syndication/feeds/stations-facilities.xml?app_id=3a0c4a01&app_key=ea95c6674605181c5dde64c7bb5d883c")
    r2 = requests.get("https://tfl.gov.uk/tfl/syndication/feeds/step-free-tube-guide.xml")

    with open('datos/stations-facilities.xml', 'wb') as f:
       f.write(r1.content)
    with open('datos/step-free-tube-guide.xml', 'wb') as f:
       f.write(r2.content)

def cleanStations():
    tree = etree()
    tree.parse("./datos/stations-facilities.xml")
    root = tree.getroot()
    search = ".//openingHours"
    for stat in tree.findall(search):
        parent = root.find(search+"/..")
        if parent:
            parent.remove(stat)

    tree.write('./datos/StationFacilitiesNOH.xml')

def cleanTube():

    ET.register_namespace('xsi', "http://www.w3.org/2001/XMLSchema-instance")
    ET.register_namespace("", "ELRAD")
    tree2 = ET.ElementTree()
    tree2.parse("datos/step-free-tube-guide.xml")
    root2 = tree2.getroot()

    for estacion2 in root2.findall('{ELRAD}Station'):
        access = estacion2.find('{ELRAD}Accessibility')
        access_type = access.find('{ELRAD}AccessibilityType')
        if (access_type.text == 'None'):
            access.remove(access_type)

    tree2.write('./datos/StepFreeTubeNNone.xml')

def addSubElements(treePos, element):

    if "stationname" not in element.tag.lower():
        newElement = ET.SubElement(treePos, element.tag.lower().replace("ns0:", ""))
        for attribute,value in element.attrib.items():
            newElement.set(attribute.replace("ns0:", ""), value)
        try:
            e = element[0]
            for subelement in element:
                addSubElements(newElement, subelement)

        except IndexError:
            newElement.text = element.text

def facilitiesDict():

    facilites_dict = {}
    tree3 = ET.ElementTree()
    tree3.parse('datos/StationFacilitiesNOH.xml')
    facilities_root = tree3.getroot()

    for element in facilities_root:
        if element.tag == "stations":
            for station in element:
                if station.tag == "station":
                    if station[0].text.strip().lower() not in facilites_dict:
                        facilites_dict[station[0].text.strip().lower()] = station
                    else:
                        facilites_dict[station[0].text.strip().lower()] = [
                            facilites_dict[station[0].text.strip().lower()],
                            station
                        ]
    return facilites_dict

def stationsDict():

    freetube_dict = {}
    ET.register_namespace('xsi', "http://www.w3.org/2001/XMLSchema-instance")
    ET.register_namespace("", "elrad")

    tree4 = ET.ElementTree()
    tree4.parse('datos/StepFreeTubeNNone.xml')
    free_root = tree4.getroot()

    for element in free_root:
        if "Station" in element.tag:
            if element[0].text.strip().lower() not in freetube_dict:
                freetube_dict[element[0].text.strip().lower()] = element
            else:
                freetube_dict[element[0].text.strip().lower()] = [
                    freetube_dict[element[0].text.strip().lower()],
                    element
                ]
    return freetube_dict

def indent(elem, level=0):
    i = "\n" + level * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

def tflGenerator():

    facilites_dict = facilitiesDict()
    freetube_dict = stationsDict()

    root = ET.Element("stations")

    for stationName, element in facilites_dict.items():
        station = ET.SubElement(root, "station")

        for subelement in element:
            addSubElements(station, subelement)

        try:
            for subelement in freetube_dict.get(stationName):
                addSubElements(station, subelement)
        except:
            pass

    ET.register_namespace('', "elrad")
    indent(root)
    tree = ET.ElementTree(root)
    tree.write("datos/TFLfacilities.xml")


if __name__ == '__main__':

    getData()
    cleanStations()
    cleanTube()
    tflGenerator()

