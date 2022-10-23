<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entidad: FabricaciónMáquina  
===========================<!-- /10-Header -->  
<!-- 15-License -->  
[Licencia abierta](https://github.com/smart-data-models//dataModel.ManufacturingMachine/blob/master/ManufacturingMachine/LICENSE.md)  
[documento generado automáticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descripción global: **Descripción de una máquina genérica**  
versión: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Lista de propiedades  

<sup><sub>[*] Si no hay un tipo en un atributo es porque puede tener varios tipos o diferentes formatos/patrones</sub></sup>  
- `address[object]`: La dirección postal  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nombre alternativo para este artículo  - `areaServed[string]`: La zona geográfica en la que se presta un servicio o se ofrece un artículo  . Model: [https://schema.org/Text](https://schema.org/Text)- `assetIdentifier[string]`: Un identificador de activos (por ejemplo, número de etiqueta de activo) asignado por el propietario.  . Model: [https://schema.org/Text](https://schema.org/Text)- `batteryLevel[number]`: Nivel de batería. Debe ser igual a: 1.0 Cuando la carga de la batería está llena. 0.0 Cuando la carga de la batería está vacía. Nulo cuando no se puede determinar.  . Model: [https://schema.org/Number](https://schema.org/Number)- `building[*]`: Referencia a la instancia de la entidad del edificio en la que está instalada esta máquina  - `countryOfManufacture[string]`: El país donde se fabricó esta máquina.  . Model: [https://schema.org/Text](https://schema.org/Text)- `current[number]`: La corriente de alimentación nominal necesaria (a la tensión de alimentación nominal), en amperios  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated[string]`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified[string]`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description[string]`: Una descripción de este artículo  - `factory[string]`: El nombre/código de la fábrica que fabrica esta máquina.  . Model: [https://schema.org/Text](https://schema.org/Text)- `firmwareVersion[string]`: La versión de firmware (específica del fabricante) de esta máquina.  . Model: [https://schema.org/Text](https://schema.org/Text)- `firstUsedAt[string]`: Indica la fecha/hora en la que la máquina fue utilizada por primera vez (nominalmente en UTC).  . Model: [https://schema.org/Text](https://schema.org/Text)- `hardwareVersion[string]`: La versión de hardware (específica del fabricante) de esta máquina.  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: Identificador único de la entidad  - `installationNotes[object]`: Notas relativas a la instalación de esta máquina.  . Model: [https://schema.org/Text](https://schema.org/Text)- `installedAt[string]`: Indica la fecha/hora en que se instaló la máquina (nominalmente en UTC).  . Model: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: Referencia Geojson al elemento. Puede ser Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `machineModel[*]`: Una referencia al Modelo de Máquina asociado para esta máquina.  - `machineOwner[array]`: Referencia al propietario o propietarios de la máquina como persona u organización de Schema.org.  - `manufacturedAt[string]`: Indica la fecha/hora en que se fabricó la máquina (nominalmente en UTC).  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: El nombre de este artículo.  - `online[boolean]`: El estado de la comunicación de esta máquina. Una representación lógica de Offline (falso) u Online (verdadero).  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `osVersion[string]`: La versión del sistema operativo (específico del fabricante) de esta máquina  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `power[number]`: El consumo de potencia nominal de la máquina en kW  . Model: [https://schema.org/Number](https://schema.org/Number)- `rotationalSpeed[number]`:  	La velocidad máxima de rotación en rpm (para máquinas como taladros, tornos)  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `serialNumber[string]`: El número de serie asignado por el fabricante.  . Model: [https://schema.org/Text](https://schema.org/Text)- `softwareVersion[string]`: La versión de software (específica del fabricante) de esta máquina.  . Model: [https://schema.org/Text](https://schema.org/Text)- `source[string]`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen o la URL del objeto de origen.  - `status[string]`: Código de estado de la máquina con formato de texto (actual) o descripción. Se espera que sea el código de estado específico del fabricante o de la máquina generado por ésta.  . Model: [https://schema.org/Text](https://schema.org/Text)- `subscriptionService[array]`: Referencia a las suscripciones de servicios relacionados con esta máquina, por ejemplo, suministros de energía, proveedores de servicios de Internet, etc., mantenimiento  - `supplierName[string]`: El nombre del proveedor de esta máquina.  . Model: [https://schema.org/Text](https://schema.org/Text)- `supportedProtocol[array]`: Protocolo(s) o redes soportados.  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: Tipo de entidad NGSI. Tiene que ser ManufacturingMachine.  - `voltage[number]`: La tensión nominal de alimentación necesaria, en voltios  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propiedades requeridas  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Este modelo de datos procede del proyecto original de GSMA IoT, https://www.gsma.com/iot/iot-big-data/. Hay algunas adaptaciones menores para cumplir los requisitos de los modelos de datos inteligentes.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ManufacturingMachine:    
  description: 'Description of a generic machine'    
  properties:    
    address:    
      description: 'The mailing address'    
      properties:    
        addressCountry:    
          description: 'Property. The country. For example, Spain. Model:''https://schema.org/addressCountry'''    
          type: string    
        addressLocality:    
          description: 'Property. The locality in which the street address is, and which is in the region. Model:''https://schema.org/addressLocality'''    
          type: string    
        addressRegion:    
          description: 'Property. The region in which the locality is, and which is in the country. Model:''https://schema.org/addressRegion'''    
          type: string    
        postOfficeBoxNumber:    
          description: 'Property. The post office box number for PO box addresses. For example, 03578. Model:''https://schema.org/postOfficeBoxNumber'''    
          type: string    
        postalCode:    
          description: 'Property. The postal code. For example, 24004. Model:''https://schema.org/https://schema.org/postalCode'''    
          type: string    
        streetAddress:    
          description: 'Property. The street address. Model:''https://schema.org/streetAddress'''    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: 'The geographic area where a service or offered item is provided'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    assetIdentifier:    
      description: 'An asset identifier (e.g. asset tag number) assigned by the owner.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    batteryLevel:    
      description: 'Battery level. It must be equal to: 1.0 When the battery charge is full. 0.0 When the battery charge empty. Null when it cannot be determined.'    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    building:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to the building entity instance into which this machine is installed'    
      x-ngsi:    
        type: Relationship    
    countryOfManufacture:    
      description: 'The country where this machine was manufactured.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    current:    
      description: 'The nominal required supply current (at the nominal supply voltage), in amps'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Amps    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    factory:    
      description: 'The factory name/code manufacturing this machine.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    firmwareVersion:    
      description: 'The (manufacturer specific) firmware version of this machine.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    firstUsedAt:    
      description: 'Indicates the date/time at which date and time the machine was first used (nominally in UTC).'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    hardwareVersion:    
      description: 'The (manufacturer specific) hardware version of this machine.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    id:    
      anyOf: &manufacturingmachine_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      x-ngsi:    
        type: Property    
    installationNotes:    
      description: 'Notes relating to this machine installation.'    
      properties:    
        docUri:    
          format: uri    
          type: string    
        value:    
          type: string    
      type: object    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    installedAt:    
      description: 'Indicates the date/time at which date and time the machine was installed (nominally in UTC).'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: 'Geoproperty. Geojson reference to the item. Point'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                type: number    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - Point    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Point'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. LineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              minItems: 2    
              type: array    
            type:    
              enum:    
                - LineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON LineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. Polygon'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 4    
                type: array    
              type: array    
            type:    
              enum:    
                - Polygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON Polygon'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiPoint'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  type: number    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPoint    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPoint'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    type: number    
                  minItems: 2    
                  type: array    
                minItems: 2    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiLineString    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiLineString'    
          type: object    
        - description: 'Geoproperty. Geojson reference to the item. MultiLineString'    
          properties:    
            bbox:    
              items:    
                type: number    
              minItems: 4    
              type: array    
            coordinates:    
              items:    
                items:    
                  items:    
                    items:    
                      type: number    
                    minItems: 2    
                    type: array    
                  minItems: 4    
                  type: array    
                type: array    
              type: array    
            type:    
              enum:    
                - MultiPolygon    
              type: string    
          required:    
            - type    
            - coordinates    
          title: 'GeoJSON MultiPolygon'    
          type: object    
      x-ngsi:    
        type: Geoproperty    
    machineModel:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'A reference to the associated Machine Model for this machine.'    
      x-ngsi:    
        type: Relationship    
    machineOwner:    
      description: 'Reference to the owner or owners of the machine as either a Schema.org person or organization.'    
      items:    
        anyOf:    
          - description: 'Property. Identifier format of any NGSI entity'    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
          - description: 'Property. Identifier format of any NGSI entity'    
            format: uri    
            type: string    
      type: array    
      x-ngsi:    
        type: Relationship    
    manufacturedAt:    
      description: 'Indicates the date/time at which date and time the machine was manufactured (nominally in UTC).'    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    online:    
      description: 'The communication status of this machine. A logical representation of Offline (false) or Online (true).'    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean    
        type: Property    
    osVersion:    
      description: 'The (manufacturer specific) operating system version of this machine'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *manufacturingmachine_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    power:    
      description: 'The nominal rated power consumption of the machine in kW'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Kw    
    rotationalSpeed:    
      description: ' 	The maximum rotational speed in rpm (for machines such as drills, lathes)'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: rpm    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      x-ngsi:    
        type: Property    
    serialNumber:    
      description: 'The serial number assigned by the manufacturer.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    softwareVersion:    
      description: 'The (manufacturer specific) software version of this machine.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    status:    
      description: 'Text formatted (current) machine status code or description. Expected to be the manufacturer or machine specific status code generated by the machine.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    subscriptionService:    
      description: 'Reference to service subscriptions related to this machine e.g. energy supplies, Internet Service Providers etc, maintenance'    
      items:    
        anyOf:    
          - description: 'Property. Identifier format of any NGSI entity'    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
          - description: 'Property. Identifier format of any NGSI entity'    
            format: uri    
            type: string    
      type: array    
      x-ngsi:    
        type: Relationship    
    supplierName:    
      description: 'The name of the supplier of this machine.'    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    supportedProtocol:    
      description: 'Supported protocol(s) or networks.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: 'NGSI entity type. It has to be ManufacturingMachine.'    
      enum:    
        - ManufacturingMachine    
      type: string    
      x-ngsi:    
        type: Property    
    voltage:    
      description: 'The nominal required supply voltage, in volts'    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
        units: Volts    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.ManufacturingMachine/blob/master/ManufacturingMachine/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.ManufacturingMachine/ManufacturingMachine/schema.json    
  x-model-tags: GSMA    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Ejemplo de carga útil  
#### ManufacturingMachine NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de una ManufacturingMachine en formato JSON-LD como valores-clave. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "assetIdentifier": "ID12345",  
  "batteryLevel": 0.7,  
  "building": "urn:ngsi-ld:Building:8683b757-649c-49e0-ac89-ad392c9a0d0c",  
  "countryOfManufacture": "UK",  
  "current": 20,  
  "dataProvider": "https://provider.example.com",  
  "description": "Industrial machine to create plastic bottles",  
  "factory": "N9",  
  "firmwareVersion": "A.10",  
  "firstUsedAt": "2017-05-04T10:18:16Z",  
  "hardwareVersion": "2.1",  
  "id": "urn:ngsi-ld:Machine:9166c528-9c98-4579-a5d3-8068aea5d6c0",  
  "installationNotes": {  
    "docUri": "http://example.com/sample/machine-instructions.pdf",  
    "value": "Installed according to manufacturer instructions."  
  },  
  "installedAt": "2017-05-04T10:18:16Z",  
  "location": {  
    "coordinates": [  
      -104.99404,  
      39.75621  
    ],  
    "type": "Point"  
  },  
  "machineModel": "urn:ngsi-ld:MachineModel:00b42701-43e1-482d-aa7a-e2956cfd69c3",  
  "manufacturedAt": "2017-05-04T10:18:16Z",  
  "online": true,  
  "osVersion": "10A",  
  "machineOwner": [  
    "urn:ngsi-ld:Person:a498182c-47c0-11e8-be4e-2c4d549a1ab2",  
    "urn:ngsi-ld:Organization:abb20712-47c0-11e8-8742-2c4d549a1ab2"  
  ],  
  "power": 4.4,  
  "rotationalSpeed": 10,  
  "serialNumber": "X9923456789F",  
  "softwareVersion": "8.5.C",  
  "source": "https://source.example.com",  
  "status": "SC1001",  
  "subscriptionService": [  
      "urn:ngsi-ld:SubscriptionService:0d95b03c-47c1-11e8-99fd-2c4d549a1ab2",  
      "urn:ngsi-ld:SubscriptionService:1527d0fa-47c1-11e8-8fb1-2c4d549a1ab2"  
    ],  
  "supplierName": "ACME NorthEast Inc.",  
  "supportedProtocol": [  
    "HTTP",  
    "HTTPS",  
    "FTP"  
  ],  
  "type": "ManufacturingMachine",  
  "voltage": 220  
}  
```  
</details>  
#### ManufacturingMachine NGSI-v2 normalizado Ejemplo  
Aquí hay un ejemplo de una ManufacturingMachine en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:Machine:9166c528-9c98-4579-a5d3-8068aea5d6c0",  
  "type": "ManufacturingMachine",  
  "source": {  
    "type": "Text",  
    "value": "https://source.example.com"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "https://provider.example.com"  
  },  
  "machineModel": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:MachineModel:00b42701-43e1-482d-aa7a-e2956cfd69c3"  
  },  
  "serialNumber": {  
    "type": "Text",  
    "value": "X9923456789F"  
  },  
  "assetIdentifier": {  
    "type": "Text",  
    "value": "ID12345"  
  },  
  "supplierName": {  
    "type": "Text",  
    "value": "ACME NorthEast Inc."  
  },  
  "countryOfManufacture": {  
    "type": "Text",  
    "value": "UK"  
  },  
  "factory": {  
    "type": "Text",  
    "value": "N9"  
  },  
  "firstUsedAt": {  
    "type": "DateTime",  
    "value": "2017-05-04T10:18:16Z"  
  },  
  "installedAt": {  
    "type": "DateTime",  
    "value": "2017-05-04T10:18:16Z"  
  },  
  "manufacturedAt": {  
    "type": "DateTime",  
    "value": "2017-05-04T10:18:16Z"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Industrial machine to create plastic bottles"  
  },  
  "owner": {  
    "type": "Relationship",  
    "value": [  
      "urn:ngsi-ld:Person:a498182c-47c0-11e8-be4e-2c4d549a1ab2",  
      "urn:ngsi-ld:Organization:abb20712-47c0-11e8-8742-2c4d549a1ab2"  
    ]  
  },  
  "hardwareVersion": {  
    "type": "Text",  
    "value": "2.1"  
  },  
  "firmwareVersion": {  
    "type": "Text",  
    "value": "A.10"  
  },  
  "softwareVersion": {  
    "type": "Text",  
    "value": "8.5.C"  
  },  
  "osVersion": {  
    "type": "Text",  
    "value": "10A"  
  },  
  "supportedProtocol": {  
    "type": "array",  
    "value": [  
      "HTTP",  
      "HTTPS",  
      "FTP"  
    ]  
  },  
  "building": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:Building:8683b757-649c-49e0-ac89-ad392c9a0d0c"  
  },  
  "location": {  
    "type": "geo:json",  
    "value": {  
      "type": "Point",  
      "coordinates": [  
        -104.99404,  
        39.75621  
      ]  
    }  
  },  
  "subscriptionService": {  
    "type": "Relationship",  
    "value": [  
      "urn:ngsi-ld:SubscriptionService:0d95b03c-47c1-11e8-99fd-2c4d549a1ab2",  
      "urn:ngsi-ld:SubscriptionService:1527d0fa-47c1-11e8-8fb1-2c4d549a1ab2"  
    ]  
  },  
  "online": {  
    "type": "Text",  
    "value": true  
  },  
  "status": {  
    "type": "Text",  
    "value": "SC1001"  
  },  
  "batteryLevel": {  
    "type": "Number",  
    "value": 0.7  
  },  
  "installationNotes": {  
    "type": "StructuredValue",  
    "value": {  
      "value": "Installed according to manufacturer instructions.",  
      "docUri": "http://example.com/sample/machine-instructions.pdf"  
    }  
  },  
  "voltage": {  
    "type": "Number",  
    "value": 220  
  },  
  "current": {  
    "type": "Text",  
    "value": 20  
  },  
  "power": {  
    "type": "Number",  
    "value": 4.4  
  },  
  "rotationalSpeed": {  
    "type": "Number",  
    "value": 10  
  }  
}  
```  
</details>  
#### ManufacturingMachine NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de una ManufacturingMachine en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "@context": [  
        "https://smartdatamodels.org/context.jsonld",  
        "https://raw.githubusercontent.com/GSMADeveloper/NGSI-LD-Entities/master/examples/Machine-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.ManufacturingMachine/master/context.jsonld"  
    ],  
    "assetIdentifier": "ID12345",  
    "batteryLevel": 0.7,  
    "building": "urn:ngsi-ld:Building:8683b757-649c-49e0-ac89-ad392c9a0d0c",  
    "countryOfManufacture": "UK",  
    "current": 20,  
    "dataProvider": "https://provider.example.com",  
    "description": "Industrial machine to create plastic bottles",  
    "factory": "N9",  
    "firmwareVersion": "A.10",  
    "firstUsedAt": "2017-05-04T10:18:16Z",  
    "hardwareVersion": "2.1",  
    "id": "urn:ngsi-ld:Machine:9166c528-9c98-4579-a5d3-8068aea5d6c0",  
    "installationNotes": {  
        "docUri": "http://example.com/sample/machine-instructions.pdf",  
        "value": "Installed according to manufacturer instructions."  
    },  
    "installedAt": "2017-05-04T10:18:16Z",  
    "location": {  
        "coordinates": [  
            -104.99404,  
            39.75621  
        ],  
        "type": "Point"  
    },  
    "machineModel": "urn:ngsi-ld:MachineModel:00b42701-43e1-482d-aa7a-e2956cfd69c3",  
    "manufacturedAt": "2017-05-04T10:18:16Z",  
    "online": true,  
    "osVersion": "10A",  
    "machineOwner": [  
        "urn:ngsi-ld:Person:a498182c-47c0-11e8-be4e-2c4d549a1ab2",  
        "urn:ngsi-ld:Organization:abb20712-47c0-11e8-8742-2c4d549a1ab2"  
    ],  
    "power": 4.4,  
    "rotationalSpeed": 10,  
    "serialNumber": "X9923456789F",  
    "softwareVersion": "8.5.C",  
    "source": "https://source.example.com",  
    "status": "SC1001",  
    "subscriptionService": [  
        "urn:ngsi-ld:SubscriptionService:0d95b03c-47c1-11e8-99fd-2c4d549a1ab2",  
        "urn:ngsi-ld:SubscriptionService:1527d0fa-47c1-11e8-8fb1-2c4d549a1ab2"  
    ],  
    "supplierName": "ACME NorthEast Inc.",  
    "supportedProtocol": [  
        "HTTP",  
        "HTTPS",  
        "FTP"  
    ],  
    "type": "ManufacturingMachine",  
    "voltage": 220  
}  
```  
</details>  
#### ManufacturingMachine NGSI-LD normalizado Ejemplo  
Este es un ejemplo de una ManufacturingMachine en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "@context": [  
        "https://smartdatamodels.org/context.jsonld",  
        "https://raw.githubusercontent.com/GSMADeveloper/NGSI-LD-Entities/master/examples/Machine-context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.ManufacturingMachine/master/context.jsonld"  
    ],  
    "id": "urn:ngsi-ld:Machine:9166c528-9c98-4579-a5d3-8068aea5d6c0",  
    "type": "ManufacturingMachine",  
    "source": {  
        "type": "Property",  
        "value": "https://source.example.com"  
    },  
    "dataProvider": {  
        "type": "Property",  
        "value": "https://provider.example.com"  
    },  
    "machineModel": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:MachineModel:00b42701-43e1-482d-aa7a-e2956cfd69c3"  
    },  
    "serialNumber": {  
        "type": "Property",  
        "value": "X9923456789F"  
    },  
    "assetIdentifier": {  
        "type": "Property",  
        "value": "ID12345"  
    },  
    "supplierName": {  
        "type": "Property",  
        "value": "ACME NorthEast Inc."  
    },  
    "countryOfManufacture": {  
        "type": "Property",  
        "value": "UK"  
    },  
    "factory": {  
        "type": "Property",  
        "value": "N9"  
    },  
    "firstUsedAt": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2017-05-04T10:18:16Z"  
        }  
    },  
    "installedAt": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2017-05-04T10:18:16Z"  
        }  
    },  
    "manufacturedAt": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2017-05-04T10:18:16Z"  
        }  
    },  
    "description": {  
        "type": "Property",  
        "value": "Industrial machine to create plastic bottles"  
    },  
    "owner": {  
        "type": "Relationship",  
        "object": [  
            "urn:ngsi-ld:Person:a498182c-47c0-11e8-be4e-2c4d549a1ab2",  
            "urn:ngsi-ld:Organization:abb20712-47c0-11e8-8742-2c4d549a1ab2"  
        ]  
    },  
    "hardwareVersion": {  
        "type": "Property",  
        "value": "2.1"  
    },  
    "firmwareVersion": {  
        "type": "Property",  
        "value": "A.10"  
    },  
    "softwareVersion": {  
        "type": "Property",  
        "value": "8.5.C"  
    },  
    "osVersion": {  
        "type": "Property",  
        "value": "10A"  
    },  
    "supportedProtocol": {  
        "type": "Property",  
        "value": [  
            "HTTP",  
            "HTTPS",  
            "FTP"  
        ],  
        "observedAt": "2017-05-04T12:30:00Z"  
    },  
    "building": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:Building:8683b757-649c-49e0-ac89-ad392c9a0d0c"  
    },  
    "location": {  
        "type": "Geoproperty",  
        "value": {  
            "type": "Point",  
            "coordinates": [  
                -104.99404,  
                39.75621  
            ]  
        }  
    },  
    "subscriptionService": {  
        "type": "Relationship",  
        "object": [  
            "urn:ngsi-ld:SubscriptionService:0d95b03c-47c1-11e8-99fd-2c4d549a1ab2",  
            "urn:ngsi-ld:SubscriptionService:1527d0fa-47c1-11e8-8fb1-2c4d549a1ab2"  
        ]  
    },  
    "online": {  
        "type": "Property",  
        "value": true,  
        "observedAt": "2017-05-04T12:30:00Z"  
    },  
    "status": {  
        "type": "Property",  
        "value": "SC1001",  
        "observedAt": "2017-05-04T12:30:00Z"  
    },  
    "batteryLevel": {  
        "type": "Property",  
        "value": 0.7,  
        "observedAt": "2017-05-04T12:30:00Z"  
    },  
    "installationNotes": {  
        "type": "Property",  
        "value": {  
            "value": "Installed according to manufacturer instructions.",  
            "docUri": "http://example.com/sample/machine-instructions.pdf"  
        }  
    },  
    "voltage": {  
        "type": "Property",  
        "value": 220,  
        "unitCode": "VLT",  
        "observedAt": "2016-08-08T10:18:16Z"  
    },  
    "current": {  
        "type": "Property",  
        "value": 20,  
        "unitCode": "AMP",  
        "observedAt": "2016-08-08T10:18:16Z"  
    },  
    "power": {  
        "type": "Property",  
        "value": 4.4,  
        "unitCode": "KWT",  
        "observedAt": "2016-08-08T10:18:16Z"  
    },  
    "rotationalSpeed": {  
        "type": "Property",  
        "value": 10,  
        "unitCode": "RPM",  
        "observedAt": "2016-08-08T10:18:16Z"  
    }  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Consulte [FAQ 10](https://smartdatamodels.org/index.php/faqs/) para obtener una respuesta sobre cómo tratar las unidades de magnitud  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
