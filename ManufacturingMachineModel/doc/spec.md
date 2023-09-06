<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entity: ManufacturingMachineModel  
=================================<!-- /10-Header -->  
<!-- 15-License -->  
[Open License](https://github.com/smart-data-models//dataModel.ManufacturingMachine/blob/master/ManufacturingMachineModel/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Global description: **This entity contains a harmonised description of a generic machine model. This entity is primarily associated with the industry segment and related IoT applications. The machineModel includes a hierarchical structure that allows machine models to be grouped in a flexible way.**  
version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## List of properties  

<sup><sub>[*] If there is not a type in an attribute is because it could have several types or different formats/patterns</sub></sup>  
- `address[object]`: The mailing address  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: The country. For example, Spain  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)  
	- `addressLocality[string]`: The locality in which the street address is, and which is in the region  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)  
	- `addressRegion[string]`: The region in which the locality is, and which is in the country  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)  
	- `district[string]`: A district is a type of administrative division that, in some countries, is managed by the local government    
	- `postOfficeBoxNumber[string]`: The post office box number for PO box addresses. For example, 03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)  
	- `postalCode[string]`: The postal code. For example, 24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)  
	- `streetAddress[string]`: The street address  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)  
- `alternateName[string]`: An alternative name for this item  - `areaServed[string]`: The geographic area where a service or offered item is provided  . Model: [https://schema.org/Text](https://schema.org/Text)- `brandName[string]`: The brand name of this MachineModel  - `dataProvider[string]`: A sequence of characters identifying the provider of the harmonised data entity  - `dateCreated[date-time]`: Entity creation timestamp. This will usually be allocated by the storage platform  - `dateModified[date-time]`: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform  - `description[string]`: A description of this item  - `documentation[string]`: Reference to data sheet or other manufacturer’s documentation about this MachineModel  - `id[*]`: Unique identifier of the entity  - `location[*]`: Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon  - `machineModelChildren[array]`: References any lower level MachineModel entities that are based on this machine model  - `machineModelParent[*]`: References any higher level MachineModel that this machine model is based on  - `manufacturerName[string]`: The name of manufacturer of this MachineModel  - `manufacturingMachineType[array]`: A List of functional categories which this machineModel supports. Enum:'robot, cnc, 2dPrinter, 3dPrinter, 3dScanner, lathe, injectionMolding, laserCutter, millingMachine, grindingMachine, stampingMachine, oven, kiln, packaging, mixer, dryer, fan, saw'  - `name[string]`: The name of this item  - `owner[array]`: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)  - `processDescription[string]`: A description of the industrial process carried out by this machine  - `root[boolean]`: A logical indicator that this Manufacturing Machine Model is the root of a Machine Model hierarchy.True indicates it is the root, false indicates that it is not the root  - `seeAlso[*]`: list of uri pointing to additional resources about the item  - `source[string]`: A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object  - `standardOperations[array]`: Lists the standard set of operations supported by this machineModel  - `type[string]`: NGSI Entity identifier. It has to be ManufacturingMachineModel  - `version[string]`: The manufacturer defined version number for the machine model  <!-- /30-PropertiesList -->  
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
ManufacturingMachineModel:    
  description: This entity contains a harmonised description of a generic machine model. This entity is primarily associated with the industry segment and related IoT applications. The machineModel includes a hierarchical structure that allows machine models to be grouped in a flexible way.    
  properties:    
    address:    
      description: The mailing address    
      properties:    
        addressCountry:    
          description: 'The country. For example, Spain'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressCountry    
            type: Property    
        addressLocality:    
          description: 'The locality in which the street address is, and which is in the region'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressLocality    
            type: Property    
        addressRegion:    
          description: 'The region in which the locality is, and which is in the country'    
          type: string    
          x-ngsi:    
            model: https://schema.org/addressRegion    
            type: Property    
        district:    
          description: 'A district is a type of administrative division that, in some countries, is managed by the local government'    
          type: string    
          x-ngsi:    
            type: Property    
        postOfficeBoxNumber:    
          description: 'The post office box number for PO box addresses. For example, 03578'    
          type: string    
          x-ngsi:    
            model: https://schema.org/postOfficeBoxNumber    
            type: Property    
        postalCode:    
          description: 'The postal code. For example, 24004'    
          type: string    
          x-ngsi:    
            model: https://schema.org/https://schema.org/postalCode    
            type: Property    
        streetAddress:    
          description: The street address    
          type: string    
          x-ngsi:    
            model: https://schema.org/streetAddress    
            type: Property    
        streetNr:    
          description: Number identifying a specific property on a public street    
          type: string    
          x-ngsi:    
            type: Property    
      type: object    
      x-ngsi:    
        model: https://schema.org/address    
        type: Property    
    alternateName:    
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    areaServed:    
      description: The geographic area where a service or offered item is provided    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    brandName:    
      description: The brand name of this MachineModel    
      type: string    
      x-ngsi:    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    documentation:    
      description: Reference to data sheet or other manufacturer’s documentation about this MachineModel    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    location:    
      description: 'Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon'    
      oneOf:    
        - description: Geojson reference to the item. Point    
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
          title: GeoJSON Point    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. LineString    
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
          title: GeoJSON LineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. Polygon    
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
          title: GeoJSON Polygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiPoint    
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
          title: GeoJSON MultiPoint    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
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
          title: GeoJSON MultiLineString    
          type: object    
          x-ngsi:    
            type: GeoProperty    
        - description: Geojson reference to the item. MultiLineString    
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
          title: GeoJSON MultiPolygon    
          type: object    
          x-ngsi:    
            type: GeoProperty    
      x-ngsi:    
        type: GeoProperty    
    machineModelChildren:    
      description: References any lower level MachineModel entities that are based on this machine model    
      items:    
        anyOf:    
          - description: Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
            x-ngsi:    
              type: Property    
          - description: Identifier format of any NGSI entity    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
      type: array    
      x-ngsi:    
        type: Relationship    
    machineModelParent:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: References any higher level MachineModel that this machine model is based on    
      x-ngsi:    
        type: Relationship    
    manufacturerName:    
      description: The name of manufacturer of this MachineModel    
      type: string    
      x-ngsi:    
        type: Property    
    manufacturingMachineType:    
      description: 'A List of functional categories which this machineModel supports. Enum:''robot, cnc, 2dPrinter, 3dPrinter, 3dScanner, lathe, injectionMolding, laserCutter, millingMachine, grindingMachine, stampingMachine, oven, kiln, packaging, mixer, dryer, fan, saw'''    
      items:    
        enum:    
          - 2dPrinter    
          - 3dPrinter    
          - 3dScanner    
          - cnc    
          - dryer    
          - fan    
          - grindingMachine    
          - injectionMolding    
          - kiln    
          - laserCutter    
          - lathe    
          - millingMachine    
          - mixer    
          - oven    
          - packaging    
          - robot    
          - saw    
          - stampingMachine    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf:    
          - description: Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
            x-ngsi:    
              type: Property    
          - description: Identifier format of any NGSI entity    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
        description: Unique identifier of the entity    
        x-ngsi:    
          type: Property    
      type: array    
      x-ngsi:    
        type: Property    
    processDescription:    
      description: A description of the industrial process carried out by this machine    
      type: string    
      x-ngsi:    
        type: Property    
    root:    
      description: 'A logical indicator that this Manufacturing Machine Model is the root of a Machine Model hierarchy.True indicates it is the root, false indicates that it is not the root'    
      type: boolean    
      x-ngsi:    
        type: Property    
    seeAlso:    
      description: list of uri pointing to additional resources about the item    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    standardOperations:    
      description: Lists the standard set of operations supported by this machineModel    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI Entity identifier. It has to be ManufacturingMachineModel    
      enum:    
        - ManufacturingMachineModel    
      type: string    
      x-ngsi:    
        type: Property    
    version:    
      description: The manufacturer defined version number for the machine model    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.ManufacturingMachine/blob/master/ManufacturingMachineModel/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.ManufacturingMachine/ManufacturingMachineModel/schema.json    
  x-model-tags: GSMA    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Example payloads    
#### ManufacturingMachineModel NGSI-v2 key-values Example    
Here is an example of a ManufacturingMachineModel in JSON-LD format as key-values. This is compatible with NGSI-v2 when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:MachineModel:e01f13d1-fea4-4cc4-92c9-0d9fadb2c509",  
  "type": "ManufacturingMachineModel",  
  "source": "https://source.example.com",  
  "dataProvider": "https://provider.example.com",  
  "name": "CA1256b",  
  "documentation": "https://example.com",  
  "description": "Machine to screen print t-shirts",  
  "manufacturerName": "ScreenOPrint, Inc.",  
  "brandName": "QuickT",  
  "version": "v1",  
  "manufacturingMachineType": [  
    "2dPrinter"  
  ],  
  "root": false,  
  "machineModelParent": "urn:ngsi-ld:MachineModel:4146335f-839f-4ff9-a575-6b4e6232b734",  
  "machineModelChildren": [  
    "urn:ngsi-ld:MachineModel:a74fcf24-58fa-11e8-ae3e-df1abd78f83f",  
    "urn:ngsi-ld:MachineModel:b29330f6-58fa-11e8-93b5-1379ded6eef6"  
  ],  
  "processDescription": "Industrial printer used to mass print t-shirts",  
  "standardOperations": [  
    "print"  
  ]  
}  
```  
</details>  
#### ManufacturingMachineModel NGSI-v2 normalized Example    
Here is an example of a ManufacturingMachineModel in JSON-LD format as normalized. This is compatible with NGSI-v2 when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
  "id": "urn:ngsi-ld:MachineModel:e01f13d1-fea4-4cc4-92c9-0d9fadb2c509",  
  "type": "ManufacturingMachineModel",  
  "source": {  
    "type": "URL",  
    "value": "https://source.example.com"  
  },  
  "dataProvider": {  
    "type": "URL",  
    "value": "https://provider.example.com"  
  },  
  "name": {  
    "type": "Text",  
    "value": "CA1256b"  
  },  
  "documentation": {  
    "type": "Text",  
    "value": "https://example.com"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Machine to screen print t-shirts"  
  },  
  "manufacturerName": {  
    "type": "Text",  
    "value": "ScreenOPrint, Inc."  
  },  
  "brandName": {  
    "type": "Text",  
    "value": "QuickT"  
  },  
  "version": {  
    "type": "Text",  
    "value": "v1"  
  },  
  "manufacturingMachineType": {  
    "type": "array",  
    "value": [  
      "2dPrinter"  
    ]  
  },  
  "root": {  
    "type": "Boolean",  
    "value": false  
  },  
  "machineModelParent": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:MachineModel:4146335f-839f-4ff9-a575-6b4e6232b734"  
  },  
  "machineModelChildren": {  
    "type": "Relationship",  
    "value": [  
      "urn:ngsi-ld:MachineModel:a74fcf24-58fa-11e8-ae3e-df1abd78f83f",  
      "urn:ngsi-ld:MachineModel:b29330f6-58fa-11e8-93b5-1379ded6eef6"  
    ]  
  },  
  "processDescription": {  
    "type": "Text",  
    "value": "Industrial printer used to mass print t-shirts"  
  },  
  "standardOperations": {  
    "type": "array",  
    "value": [  
      "print"  
    ]  
  }  
}  
```  
</details>  
#### ManufacturingMachineModel NGSI-LD key-values Example    
Here is an example of a ManufacturingMachineModel in JSON-LD format as key-values. This is compatible with NGSI-LD when  using `options=keyValues` and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "@context": [  
        "https://smartdatamodels.github.io/dataModel.Transportation/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.ManufacturingMachine/master/context.jsonld"  
    ],  
    "id": "urn:ngsi-ld:MachineModel:e01f13d1-fea4-4cc4-92c9-0d9fadb2c509",  
    "type": "ManufacturingMachineModel",  
    "source": "https://source.example.com",  
    "dataProvider": "https://provider.example.com",  
    "name": "CA1256b",  
    "documentation": "https://example.com",  
    "description": "Machine to screen print t-shirts",  
    "manufacturerName": "ScreenOPrint, Inc.",  
    "brandName": "QuickT",  
    "version": "v1",  
    "manufacturingMachineType": [  
        "2dPrinter"  
    ],  
    "root": false,  
    "machineModelParent": "urn:ngsi-ld:MachineModel:4146335f-839f-4ff9-a575-6b4e6232b734",  
    "machineModelChildren": [  
        "urn:ngsi-ld:MachineModel:a74fcf24-58fa-11e8-ae3e-df1abd78f83f",  
        "urn:ngsi-ld:MachineModel:b29330f6-58fa-11e8-93b5-1379ded6eef6"  
    ],  
    "processDescription": "Industrial printer used to mass print t-shirts",  
    "standardOperations": [  
        "print"  
    ]  
}  
```  
</details>  
#### ManufacturingMachineModel NGSI-LD normalized Example    
Here is an example of a ManufacturingMachineModel in JSON-LD format as normalized. This is compatible with NGSI-LD when not using options and returns the context data of an individual entity.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "@context": [  
        "https://smartdatamodels.github.io/dataModel.Transportation/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.ManufacturingMachine/master/context.jsonld"  
    ],  
    "id": "urn:ngsi-ld:MachineModel:e01f13d1-fea4-4cc4-92c9-0d9fadb2c509",  
    "type": "ManufacturingMachineModel",  
    "source": {  
        "type": "Property",  
        "value": "https://source.example.com"  
    },  
    "dataProvider": {  
        "type": "Property",  
        "value": "https://provider.example.com"  
    },  
    "name": {  
        "type": "Property",  
        "value": "CA1256b"  
    },  
    "documentation": {  
        "type": "Property",  
        "value": "https://example.com"  
    },  
    "description": {  
        "type": "Property",  
        "value": "Machine to screen print t-shirts"  
    },  
    "manufacturerName": {  
        "type": "Property",  
        "value": "ScreenOPrint, Inc."  
    },  
    "brandName": {  
        "type": "Property",  
        "value": "QuickT"  
    },  
    "version": {  
        "type": "Property",  
        "value": "v1"  
    },  
    "manufacturingMachineType": {  
        "type": "Property",  
        "value": [  
            "2dPrinter"  
        ]  
    },  
    "root": {  
        "type": "Property",  
        "value": false  
    },  
    "machineModelParent": {  
        "type": "Relationship",  
        "object": "urn:ngsi-ld:MachineModel:4146335f-839f-4ff9-a575-6b4e6232b734"  
    },  
    "machineModelChildren": {  
        "type": "Relationship",  
        "object": [  
            "urn:ngsi-ld:MachineModel:a74fcf24-58fa-11e8-ae3e-df1abd78f83f",  
            "urn:ngsi-ld:MachineModel:b29330f6-58fa-11e8-93b5-1379ded6eef6"  
        ]  
    },  
    "processDescription": {  
        "type": "Property",  
        "value": "Industrial printer used to mass print t-shirts"  
    },  
    "standardOperations": {  
        "type": "Property",  
        "value": [  
            "print"  
        ]  
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
