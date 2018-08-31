from rdflib import Graph,URIRef, BNode, Literal, Namespace
from xml.etree.ElementTree import ElementTree as etree

tree = etree()
TFLfacilities = tree.parse("datos/TFLfacilities.xml")
root = tree.getroot()


g = Graph()
ns = Namespace("http://tfl.gov.uk/tfl/")


belongsTo = ns.belongsTo
hasStations = ns.hasStations
hasLines = ns.hasLines
hasPublicToilet = ns.hasPublicToilet
hasContactDetails = ns.hasContactDetails
hasName = ns.hasName
hasAddress = ns.hasAddress
hasPhone = ns.hasPhone
hasFacilities = ns.hasFacilities
hasFacility = ns.hasFacility
hasTicketHalls = ns.hasTicketHalls
hasLifts = ns.hasLifts
hasGates = ns.hasGates
hasToilets = ns.hasToilets
hasCashMachines = ns.hasCashMachines
hasPayphones = ns.hasPayphones
hasCarkPark = ns.hasCarkPark
hasVendingMachines = ns.hasVendingMachines
hasHelpPoints = ns.hasHelpPoints
hasWaitingRoom = ns.hasWaitingRoom
hasLocation = ns.hasLocation
isPaymentRequired = ns.isPaymentRequired
hasEntrances = ns.hasEntrances
hasEntrance = ns.hasEntrance
hasLineName = ns.hasLineName
directionTo = ns.directionTo
directionTowards = ns.directionTowards
infoAccessibility = ns.infoAccessibility
hasLine = ns.hasLine


for stations in root.findall('{elrad}station'):
    station_name = URIRef(stations.find('{elrad}name').text + ' station')

    # contact
    g.add((station_name, hasAddress, Literal(root.find('.//{elrad}address').text)))
    g.add((station_name, hasPhone, Literal(root.find('.//{elrad}phone').text)))

    #toilet
    if root.find('.//{elrad}publictoilet').attrib == {'Exists': 'Yes'}:
        g.add((station_name, hasPublicToilet, Literal('yes')))
        g.add((station_name, hasLocation, Literal(root.find('.//{elrad}location').text)))
        g.add((station_name, isPaymentRequired, Literal(root.find('.//{elrad}paymentrequired').text)))
    else:
        g.add((station_name, hasPublicToilet, Literal('no')))

    #facilities
    if station_name.find('.//{elrad}facilities'):
        g.add((station_name, hasFacilities, Literal(station_name + ' facilities')))
        g.add((URIRef(station_name + ' facilities'), hasLifts, Literal(root.find('.//{elrad}facility/[@name="Lifts"]').text)))
        g.add((URIRef(station_name + ' facilities'), hasGates, Literal(root.find('.//{elrad}facility/[@name="Gates"]').text)))
        g.add((URIRef(station_name + ' facilities'), hasVendingMachines, Literal(root.find('.//{elrad}facility/[@name="Vending Machines"]').text)))
        g.add((URIRef(station_name + ' facilities'), hasHelpPoints, Literal(root.find('.//{elrad}facility/[@name="Help Points"]').text)))
    else:
        g.add((station_name, hasFacilities, Literal('no')))

    #entrance
    if root.findall('.//{elrad}entrances'):
        entrances = root.findall('.//{elrad}entrances')
        g.add((station_name, hasEntrances,Literal(len(entrances))))
        for entrance in entrances:
            try:
                g.add((URIRef(station_name + ' entrance'),hasEntrance,Literal(entrance.find('{elrad}name').text)))
            except:
                pass

    # line
    if stations.find('.//{elrad}line'):
        linea = stations.find('.//{elrad}linename').text
        g.add((station_name, belongsTo, Literal(linea + ' line')))
        g.add((URIRef(linea + ' line'), hasStations, Literal(station_name)))
        g.add((URIRef(linea + ' line'), directionTo, Literal(root.find('.//{elrad}direction').text)))
        g.add((URIRef(linea + ' line'), directionTowards, Literal(root.find('.//{elrad}directiontowards').text)))


g.serialize(destination="datos/RDF_XML.xml",format="xml")

