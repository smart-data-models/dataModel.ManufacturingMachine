<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: ManufacturingMachine  
============================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.ManufacturingMachine/blob/master/ManufacturingMachine/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **Description of a generic machine**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `address[object]`: The mailing address  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: An alternative name for this item  - `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `assetIdentifier[string]`: An asset identifier (e.g. asset tag number) assigned by the owner.  . Model: [https://schema.org/Text](https://schema.org/Text)- `batteryLevel[number]`: Battery level. It must be equal to: 1.0 When the battery charge is full. 0.0 When the battery charge empty. Null when it cannot be determined.  . Model: [https://schema.org/Number](https://schema.org/Number)- `building[*]`: Reference to the building entity instance into which this machine is installed  - `countryOfManufacture[string]`: The country where this machine was manufactured.  . Model: [https://schema.org/Text](https://schema.org/Text)- `current[number]`: The nominal required supply current (at the nominal supply voltage), in amps  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity.  - `dateCreated[string]`: Entity creation timestamp. This will usually be allocated by the storage platform.  - `dateModified[string]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.  - `description[string]`: A description of this item  - `factory[string]`: The factory name/code manufacturing this machine.  . Model: [https://schema.org/Text](https://schema.org/Text)- `firmwareVersion[string]`: The (manufacturer specific) firmware version of this machine.  . Model: [https://schema.org/Text](https://schema.org/Text)- `firstUsedAt[string]`: Indicates the date/time at which date and time the machine was first used (nominally in UTC).  . Model: [https://schema.org/Text](https://schema.org/Text)- `hardwareVersion[string]`: The (manufacturer specific) hardware version of this machine.  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: Unique identifier of the entity  - `installationNotes[object]`: Notes relating to this machine installation.  . Model: [https://schema.org/Text](https://schema.org/Text)- `installedAt[string]`: Indicates the date/time at which date and time the machine was installed (nominally in UTC).  . Model: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `machineModel[*]`: A reference to the associated Machine Model for this machine.  - `machineOwner[array]`: Reference to the owner or owners of the machine as either a Schema.org person or organization.  - `manufacturedAt[string]`: Indicates the date/time at which date and time the machine was manufactured (nominally in UTC).  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: The name of this item.  - `online[boolean]`: The communication status of this machine. A logical representation of Offline (false) or Online (true).  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `osVersion[string]`: The (manufacturer specific) operating system version of this machine  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `power[number]`: The nominal rated power consumption of the machine in kW  . Model: [https://schema.org/Number](https://schema.org/Number)- `rotationalSpeed[number]`:  	The maximum rotational speed in rpm (for machines such as drills, lathes)  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: list of uri pointing to additional resources about the item  - `serialNumber[string]`: The serial number assigned by the manufacturer.  . Model: [https://schema.org/Text](https://schema.org/Text)- `softwareVersion[string]`: The (manufacturer specific) software version of this machine.  . Model: [https://schema.org/Text](https://schema.org/Text)- `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.  - `status[string]`: Text formatted (current) machine status code or description. Expected to be the manufacturer or machine specific status code generated by the machine.  . Model: [https://schema.org/Text](https://schema.org/Text)- `subscriptionService[array]`: Reference to service subscriptions related to this machine e.g. energy supplies, Internet Service Providers etc, maintenance  - `supplierName[string]`: The name of the supplier of this machine.  . Model: [https://schema.org/Text](https://schema.org/Text)- `supportedProtocol[array]`: Supported protocol(s) or networks.  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: NGSI entity type. It has to be ManufacturingMachine.  - `voltage[number]`: The nominal required supply voltage, in volts  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Required properties  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
This data model comes from the original project GSMA IoT project, https://www.gsma.com/iot/iot-big-data/. There are some minor adaptations to meet requirements of smart data models.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Data Model description of properties  
Sorted alphabetically (click for details)  
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
## Example payloads    
#### ManufacturingMachine NGSI-v2 key-values Example    
Here is an example of a ManufacturingMachine in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
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
#### ManufacturingMachine NGSI-v2 normalized Example    
Here is an example of a ManufacturingMachine in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
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
#### ManufacturingMachine NGSI-LD key-values Example    
Here is an example of a ManufacturingMachine in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
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
#### ManufacturingMachine NGSI-LD normalized Example    
Here is an example of a ManufacturingMachine in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
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
See [FAQ 10](https://smartdatamodels.org/index.php/faqs/) to get an answer on how to deal with magnitude units  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
