######################################################
#       MIEMBROS QUE HAN REALIZADO LA PRÁCTICA       #
#     Paula Carballo Pérez y Ester Cortés García     #
######################################################

#PARA LA REALIZACIÓN DEL GRAFO RDF NO SE HAN COGIDO TODAS LAS
#ESTACIONES DEL XML TFLfacilities, SINO QUE SE HA CODIGO UNA
#ÚNICAMNTE PARA QUE RESULTASE MÁS SENCILLO Y FÁCIL DE
#ENTENDER EL GRAFO FINAL

import xml.etree.ElementTree as ET
from rdflib import Graph, Namespace, URIRef, BNode, Literal

ET.register_namespace('', "elrad")
facilities_xml = ET.parse("datos/TFLfacilities.xml")

g = Graph()

namespace = Namespace("http://tfl.gov.uk/tfl/")


#URIS CREADAS
station = URIRef("estacion")
line = URIRef("linea")
transport = URIRef("transporte")
contactDetails = URIRef('contactDetails')
zone = URIRef('zone')
facilities = URIRef('facilities')
entrances = URIRef('entrances')
bookingHallToPlatform = URIRef('bookingHallToPlatform')
platformToTrain = URIRef('platformToTrain')
path = URIRef('path')
placemark = URIRef('Placemark')
point = URIRef('point')
publicToilet = URIRef('PublicToilet')
lines = URIRef('Lines')
accessibility = URIRef('accessibility')
lifts = URIRef('lifts')
toilets = URIRef('toilets')
specificEntrance = URIRef('specificEntrance')
accessibleInterchanges = URIRef('accessibleInterchanges')
naptans = URIRef('naptans')
naptan = URIRef('naptan')

#PREDICADOS CREADOS
belongsTo = namespace.belongsTo
hasStations = namespace.hasStations
hasLines = namespace.hasLines
canBe = namespace.canBe
belongsToZone = namespace.belongsToZone
nameZone = namespace.nameZone
hasPublicToilet = namespace.hasPublicToilet
hasContactDetails = namespace.hasContactDetails
hasName = namespace.hasName
hasAddress = namespace.hasAddress
hasPhone = namespace.hasPhone
hasFacilities = namespace.hasFacilities
hasFacility = namespace.hasFacility
hasTicketHalls = namespace.hasTicketHalls
hasLifts = namespace.hasLifts
hasEscalators = namespace.hasEscalators
hasGates = namespace.hasGates
hasToilets = namespace.hasToilets
hasPhotoBooths = namespace.hasPhotoBooths
hasCashMachines = namespace.hasCashMachines
hasPayphones = namespace.hasPayphones
hasCarkPark = namespace.hasCarkPark
hasVendingMachines = namespace.hasVendingMachines
hasHelpPoints = namespace.hasHelpPoints
hasBridge = namespace.hasBridge
hasWaitingRoom = namespace.hasWaitingRoom
hasOtherFacilities = namespace.hasOtherFacilities
hasEntrances = namespace.hasEntrances
entranceElement = namespace.entranceElement
infoEntranceToBookingHall = namespace.infoEntranceToBookingHall
infoBookingHallToPlatform = namespace.infoBookingHallToPlatform
hasPointName = namespace.hasPointName
hasPathDescription = namespace.hasPathDescription
infoPlatformToTrain = namespace.infoPlatformToTrain
hasPlatformElem = namespace.hasPlatformElem
hasTrainName = namespace.hasTrainName
numSteps = namespace.numSteps
hasPath = namespace.hasPath
hasHeading = namespace.hasHeading
hasDescription = namespace.hasDescription
hasPoint = namespace.hasPoint
hasCoordinates = namespace.hasCoordinates
hasPlacemark = namespace.hasPlacemark
hasLocation = namespace.hasLocation
isPaymentRequired = namespace.isPaymentRequired
hasLineName = namespace.hasLineName
hasPlatform = namespace.hasPlatform
directionTo = namespace.directionTo
directionTowards = namespace.directionTowards
stepMinis = namespace.stepMinis
stepMaxis = namespace.stepMaxis
gapMinis = namespace.gapMinis
gapMaxis = namespace.gapMaxis
hasAccessbyramp = namespace.hasAccessbyramp
levelAccess = namespace.levelAccess
lineInformation = namespace.lineInformation
infoAccessibility = namespace.infoAccessibility
hasAdditionalInformation = namespace.hasAdditionalInformation
hasBlueBadgeCarParkSpaces = namespace.hasBlueBadgeCarParkSpaces
hasTaxiRanksOutsideStation = namespace.hasTaxiRanksOutsideStation
accessibilityType = namespace.accessibilityType
hasSpecificEntrance = namespace.hasSpecificEntrance
hasAccessViaLift = namespace.hasAccessViaLift
LimitedCapacityLift = namespace.LimitedCapacityLift
hasAccessibleToilet = namespace.hasAccessibleToilet
accessibleToiletNote = namespace.AccessibleToiletNote
specificEntranceRequired = namespace.specificEntranceRequired
specificEntranceInstructions = namespace.specificEntranceInstructions
hasAccessibleInterchanges = namespace.hasAccessibleInterchanges
hasAirportInterchange = namespace.hasAirportInterchange
hasPierInterchange = namespace.hasPierInterchange
hasMainBusInterchange = namespace.hasMainBusInterchange
hasEmiratesAirLineInterchange = namespace.hasEmiratesAirLineInterchange
hasTramlinkInterchange = namespace.hasTramlinkInterchange
hasNationalRailInterchange = namespace.hasNationalRailInterchange
hasLine = namespace.hasLine
hasNaptans = namespace.hasNaptans
naptanDescription = namespace.naptanDescription
naptanID = namespace.naptanID
naptanElement = namespace.naptanElement

#OBTENGO EL NOMBRE DE LA ESTACIÓN SOBRE LA QUE SE VA A REALIZAR EL EJEMPLO
test = facilities_xml.getroot()
for child_station in test.findall("{elrad}station"):
    try:

        if child_station.find("{elrad}name").text == "Acton Town":
            my_station = child_station
    except:
        pass
my_station_name = URIRef("ActonTown")

#CREO EL DIAGRAMA BÁSICO, SIN PONER DETALLES EN LA ESTACIÓN
g.add((line,hasStations,my_station_name))
g.add((line,belongsTo,transport))
g.add((transport,hasStations,my_station_name))
g.add((my_station_name,belongsTo,line))
g.add((transport,hasLines,line))
g.add((my_station_name,belongsTo,transport))

g.add((transport,canBe,Literal("Tube")))
g.add((transport,canBe,Literal("Underground")))
g.add((transport,canBe,Literal("DLR")))

#COMIENZO A AÑADIR ATRIBUTOS A LA ESTACIÓN

#NAME
g.add((my_station_name, hasName, Literal(my_station.find('{elrad}name').text)))

#CONTACT DETAILS
if my_station.find('contactDetails') != None:
    g.add((my_station_name, hasContactDetails, contactDetails))
    g.add((contactDetails,hasAddress,Literal(my_station.find('{elrad}contactDetails/address').text)))
    g.add((contactDetails,hasPhone,Literal(my_station.find('{elrad}contactDetails/phone').text)))
else:
    g.add((my_station_name, hasContactDetails, BNode()))

#ZONES
if my_station.find('{elrad}zones') != None:
    g.add((my_station_name, belongsToZone, zone))
    for zones in my_station.find('{elrad}zones'):
        zone_value = zones.text
        g.add((zone,nameZone,Literal(zone_value)))
else:
    g.add((my_station_name, belongsToZone, BNode()))

#FACILITIES
if my_station.find('{elrad}facilities') != None:
    g.add((my_station_name, hasFacilities, facilities))
    g.add((facilities,hasTicketHalls, Literal(my_station.find('{elrad}facilities/facility/[@name="Ticket Halls"]').text)))
    g.add((facilities,hasLifts, Literal(my_station.find('{elrad}facilities/facility/[@name="Lifts"]').text)))
    g.add((facilities, hasOtherFacilities, Literal(my_station.find('{elrad}facilities/facility/[@name="Escalators"]').text)))
    g.add((facilities,hasEscalators, Literal(my_station.find('{elrad}facilities/facility/[@name="Gates"]').text)))
    g.add((facilities,hasGates, Literal(my_station.find('{elrad}facilities/facility/[@name="Toilets"]').text)))
    g.add((facilities,hasToilets, Literal(my_station.find('{elrad}facilities/facility/[@name="Photo Booths"]').text)))
    g.add((facilities,hasPhotoBooths, Literal(my_station.find('{elrad}facilities/facility/[@name="Cash Machines"]').text)))
    g.add((facilities,hasCashMachines, Literal(my_station.find('{elrad}facilities/facility/[@name="Payphones"]').text)))
    g.add((facilities,hasPayphones, Literal(my_station.find('{elrad}facilities/facility/[@name="Car park"]').text)))
    g.add((facilities,hasCarkPark, Literal(my_station.find('{elrad}facilities/facility/[@name="Vending Machines"]').text)))
    g.add((facilities,hasVendingMachines, Literal(my_station.find('{elrad}facilities/facility/[@name="Help Points"]').text)))
    g.add((facilities,hasHelpPoints, Literal(my_station.find('{elrad}facilities/facility/[@name="Bridge"]').text)))
    g.add((facilities,hasBridge, Literal(my_station.find('{elrad}facilities/facility/[@name="Waiting Room"]').text)))
    g.add((facilities,hasWaitingRoom, Literal(my_station.find('{elrad}facilities/facility/[@name="Other Facilities"]').text)))
else:
    g.add((my_station_name, hasFacility, BNode()))

#ENTRANCES
if my_station.find('{elrad}entrances')!= None:
    g.add((my_station_name,hasEntrances,entrances))
    num = 0
    for entranceElem in my_station.find('{elrad}entrances'):
        num += 1
        name = 'entrance' + str(num)
        entrance = URIRef(name)
        g.add((entrances,entranceElement,entrance))
        g.add((entrance,hasName,Literal(entranceElem.find('{elrad}name').text)))
        g.add((entrance,infoEntranceToBookingHall,Literal(entranceElem.find('{elrad}entranceToBookingHall').text)))
        g.add((entrance,infoBookingHallToPlatform,bookingHallToPlatform))
        if entranceElem.find('{elrad}bookingHallToPlatform/pointName') != None:
            g.add((bookingHallToPlatform, hasPointName, Literal(entranceElem.find('{elrad}bookingHallToPlatform/pointName').text)))
        else:
            g.add((bookingHallToPlatform, hasPointName, BNode()))
        if entranceElem.find('{elrad}bookingHallToPlatform/pathDescription') != None:
            g.add((bookingHallToPlatform, hasPathDescription,Literal(entranceElem.find('{elrad}bookingHallToPlatform/pathDescription').text)))
        else:
            g.add((bookingHallToPlatform, hasPointName, BNode()))
        if entranceElem.find('{elrad}bookingHallToPlatform/path') != None:
            g.add((bookingHallToPlatform, hasPath,path ))
            g.add((path,hasHeading,Literal(entranceElem.find('{elrad}bookingHallToPlatform/path/heading').text)))
            g.add((path,hasPathDescription,Literal(entranceElem.find('{elrad}bookingHallToPlatform/path/pathDescription').text)))
        else:
            g.add((bookingHallToPlatform, hasPath, BNode()))
        g.add((entrance,infoPlatformToTrain,platformToTrain))
        num2=0
        for platformElem in entranceElem.findall('{elrad}platformToTrain'):
            num2 += 1
            name = 'platform' + str(num2)
            platformElemt = URIRef(name)
            g.add((platformToTrain,hasPlatformElem,platformElemt))
            g.add((platformElemt,hasTrainName,Literal(platformElem.find('{elrad}trainName').text)))
            g.add((platformElemt,numSteps,Literal(platformElem.find('{elrad}platformToTrainSteps').text)))
else:
    g.add((my_station_name,hasEntrances,BNode()))

#PLACE MARK
if my_station.find('Placemark') != None:
    g.add((my_station_name, hasPlacemark, placemark))
    g.add((placemark,hasName,Literal(my_station.find('{elrad}Placemark/name').text)))
    g.add((placemark,hasDescription,Literal(my_station.find('{elrad}Placemark/description').text)))
    g.add((placemark,hasPoint,point))
    g.add((point,hasCoordinates,Literal(my_station.find('{elrad}Placemark/Point/coordinates').text)))
else:
    g.add((my_station_name, hasPlacemark, BNode()))

#LINES
if my_station.find('{elrad}Lines') != None:
    g.add((my_station_name, hasLines, lines))
    num=0
    for lineElem in my_station.find('{elrad}Lines'):
        num +=1
        name='line'
        lineElement = URIRef(name+str(num))
        g.add((lines,lineInformation,lineElement))
        g.add((lineElement, hasLineName, Literal(lineElem.find('{elrad}LineName').text)))
        g.add((lineElement, hasPlatform, Literal(lineElem.find('{elrad}Platform').text)))
        g.add((lineElement, directionTo, Literal(lineElem.find('{elrad}Direction').text)))
        g.add((lineElement, directionTowards, Literal(lineElem.find('{elrad}DirectionTowards').text)))
        g.add((lineElement, stepMinis, Literal(lineElem.find('{elrad}StepMin').text)))
        g.add((lineElement, stepMaxis, Literal(lineElem.find('{elrad}StepMax').text)))
        g.add((lineElement, gapMinis, Literal(lineElem.find('{elrad}GapMin').text)))
        g.add((lineElement, gapMaxis, Literal(lineElem.find('{elrad}GapMax').text)))
        g.add((lineElement, hasAccessbyramp, Literal(lineElem.find('{elrad}LevelAccessByManualRamp').text)))
        g.add((lineElement, levelAccess, Literal(lineElem.find('{elrad}LocationOfLevelAccess').text)))
else:
    g.add((my_station_name,hasLine,BNode()))

#PUBLIC TOILET
if my_station.find('{elrad}PublicToilet') != None and my_station.find('{elrad}PublicToilet').attrib == {'Exists':'Yes'}:
    g.add((my_station_name, hasPublicToilet, publicToilet))
    g.add((publicToilet,hasLocation,Literal(my_station.find('{elrad}PublicToilet/Location').text)))
    g.add((publicToilet,isPaymentRequired,Literal(my_station.find('{elrad}PublicToilet/PaymentRequired').text)))
else:
    g.add((my_station_name, hasPublicToilet, BNode()))

#ACCESSIBILITY

if my_station.find('{elrad}Accessibility') != None:
    g.add((my_station_name,infoAccessibility,accessibility))
    g.add((accessibility,hasAdditionalInformation,Literal(my_station.find('{elrad}Accessibility/AdditionalAccessibilityInformation').text)))
    g.add((accessibility,hasBlueBadgeCarParkSpaces,Literal(my_station.find('{elrad}Accessibility/AdditionalAccessibilityInformation').text)))
    g.add((accessibility,hasTaxiRanksOutsideStation,Literal(my_station.find('{elrad}Accessibility/TaxiRanksOutsideStation').text)))
    g.add((accessibility,hasLifts,lifts))
    g.add((lifts,hasAccessViaLift,Literal(my_station.find('{elrad}Accessibility/Lifts/AccessViaLift').text)))
    g.add((lifts,LimitedCapacityLift,Literal(my_station.find('{elrad}Accessibility/Lifts/LimitedCapacityLift').text)))
    g.add((accessibility,hasToilets,toilets))
    g.add((toilets,hasAccessibleToilet,Literal(my_station.find('{elrad}Accessibility/Toilets/AccessibleToilet').text)))
    g.add((toilets,accessibleToiletNote,Literal(my_station.find('{elrad}Accessibility/Toilets/AccessibleToiletNote').text)))
    g.add((accessibility,hasSpecificEntrance,specificEntrance))
    g.add((specificEntrance,specificEntranceRequired,Literal(my_station.find('{elrad}Accessibility/SpecificEntrance/SpecificEntranceRequired').text)))
    g.add((specificEntrance,specificEntranceInstructions,Literal(my_station.find('{elrad}Accessibility/SpecificEntrance/SpecificEntranceInstructions').text)))
    if my_station.find('{elrad}Accessibility/AccessibilityType') != None:
        g.add((accessibility,accessibilityType,Literal(my_station.find('{elrad}Accessibility/AccessibilityType').text)))
    else:
        g.add((accessibility,accessibility,BNode()))
else:
    g.add((my_station,infoAccessibility,BNode()))

#ACCESSIBLE INTERCHANGES
if my_station.find('{elrad}AccessibleInterchanges') != None:
    g.add((my_station_name, hasAccessibleInterchanges,accessibleInterchanges))
    g.add((accessibleInterchanges,hasAirportInterchange,Literal(my_station.find('{elrad}AccessibleInterchanges/AirportInterchange').text)))
    g.add((accessibleInterchanges,hasPierInterchange,Literal(my_station.find('{elrad}AccessibleInterchanges/PierInterchange').text)))
    g.add((accessibleInterchanges,hasMainBusInterchange,Literal(my_station.find('{elrad}AccessibleInterchanges/MainBusInterchange').text)))
    g.add((accessibleInterchanges,hasEmiratesAirLineInterchange,Literal(my_station.find('{elrad}AccessibleInterchanges/EmiratesAirLineInterchange').text)))
    g.add((accessibleInterchanges,hasTramlinkInterchange,Literal(my_station.find('{elrad}AccessibleInterchanges/TramlinkInterchange').text)))
    g.add((accessibleInterchanges,hasNationalRailInterchange,Literal(my_station.find('{elrad}AccessibleInterchanges/NationalRailInterchange').text)))
else:
    g.add((my_station_name,hasAccessibleInterchanges,BNode()))

#NAPTANS
if my_station.find('{elrad}Naptans') != None:
    g.add((my_station_name, hasNaptans,naptans))
    num_naptan = 0
    for naptane in my_station.find('{elrad}Naptans'):
        num_naptan += 1
        name = 'naptan'+str(num_naptan)
        naptan = URIRef(name)
        g.add((naptans,naptanElement,naptan))
        g.add((naptan,naptanDescription,Literal(naptane.find('{elrad}Description').text)))
        g.add((naptan,naptanID,Literal(naptane.find('{elrad}NaptanID').text)))
else:
    g.add((my_station_name,hasNaptans,BNode()))

g.serialize(destination="RDF2_XML.xml",format="xml")
