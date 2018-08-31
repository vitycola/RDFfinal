Datos Semánticos

El objetivo de este código es el de la generación de un dataset en formato RDF/XML sobre el transporte público en
Londres, a partir de la obtención de diversos datasets y de la integración de los mismos.

CONTEXTO:

Transport for London (TfL) es el organismo del gobierno local responsable de la mayoría de los aspectos del sistema
de transportes en Londres [1]. En relación al desarrollo es conveniente conocer que TfL contempla, entre otros,
el transporte en:

    -Metro (London Underground –Tube-, https://en.wikipedia.org/wiki/London_Underground
    -Tren suburbano (London Overground, https://es.wikipedia.org/wiki/London_Overground);
    -Metro ligero (Docklands Light Railway –DLR-, https://en.wikipedia.org/wiki/Docklands_Light_Railway).

TfL sigue la tendencia actual de política de datos abiertos. Por ello ofrece la posibilidad de descargar sus datasets de
transporte público a través de APIs.

Los dos datasets origen son:

    a) Station facilites: Our station facilities feed is a Geo-coded KML feed of most London Underground, DLR and
    London Overground stations. It has station facilities and access information fo r each station.

    b) Step free tube guide data: The data contained in this feed provides information about the level of step-free
    access to platforms and trains that is available at London Underground, London Overground and DLR
    stations

DESARROLLO:

    1) Acceder a la página de datos abiertos de TfL y descargar ambos datasets a través de API mediante el programa getdata.py

    2) Generar un fichero similar a a), denominado StationFacilitiesNOH, donde no se incorpore la información
    asociada a las etiquetas <openingHours>xxxx</openingHours>, ni las propias etiquetas .

    3) Generar un fichero similar a b), denominado StepFreeTubeNNone, que no debe incorporar la información
    asociada a las etiquetas <AccessibilityType>None</AccessibilityType> (ni las propias etiquetas)
    cuando el contenido sea None.

    4) Elaborar un diagrama conceptual con las entidades y las relaciones entre dichas entidades, que soporte la
    información del dominio de este problema, es decir, teniendo en cuenta l as entidades de los ficheros
    StationFacilitiesNOH y de StepFreeTubeNNone. Para el diagrama conceptual ver la transparencia número
    76 del tema Datos Semánticos y Enlazados.

    5) Generar un fichero XML denominado TFLfacilities, resultado de la integración de los ficheros del apartado
    2 y 3.

    6) Generar un grafo RDF (que será el resultado de la integración de los ficheros antes mencionados), utilizando
    la librería rdflib. Para ello sería conveniente seguir el diagrama conceptual creado en el punto 4. El resultado
    de este último paso será un fichero RDF/XML. Hay que tener en cuenta que la información deberá integrarse
    asociando los nombres de las estaciones de a) y b) cuando estos sean iguales. A continuación se muestra
    un ejemplo para el caso concreto de una estación.

ENLACES DE INTERES:

[1]. TFL (Transport for London), Wikipedia, https://en.wikipedia.org/wiki/Transport_for_London
[2]. Página de datos abiertos de TFL (Transport for London Unified API), https://api.tfl.gov.uk/
[3]. Documentación acerca de los data feeds de TFL, https://api-portal.tfl.gov.uk/docs
[4]. Station Facilities, https://data.tfl.gov.uk/tfl/syndication/feeds/stationsfacilities.xml?app_id=3a0c4a01&app_key=ea95c6674605181c5dde64c7bb5d883c
[5]. Step Free Tube Guide, https://tfl.gov.uk/tfl/syndication/feeds/step-free-tube-guide.xml