Entité : ManufacturingMachineOperation  
======================================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.ManufacturingMachine/blob/master/ManufacturingMachineOperation/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Description globale : **Description d'une machine-opération**.  

## Liste des propriétés  

- `address`: L'adresse postale  - `alternateName`: Un nom alternatif pour cet élément  - `areaServed`: La zone géographique où un service ou un article offert est fourni  - `commandSequence`: La séquence de commande exécutée/ demandée pour la machine dans un format de représentation pertinent pour la machine.  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `endedAt`: Horodatage de la fin effective de l'opération.  - `id`: Identifiant unique de l'entité  - `location`: Référence Geojson à l'élément. Il peut s'agir d'un point, d'une ligne, d'un polygone, d'un point multiple, d'une ligne multiple ou d'un polygone multiple.  - `machine`: Une référence à la machine associée pour cette opération de machine.  - `name`: Le nom de cet élément.  - `operationOutput`: Une propriété personnalisée décrivant les données de sortie de l'opération. Les propriétés du schéma de la sortie dépendent fortement du modèle de la machine.  - `operationType`: Définit le type d'opération effectuée/ demandée. Il s'agira de l'un des types d'opération définis dans une liste spécifique à la machine/modèle de machine, y compris ceux-ci. Enum : 'processus, réglage，maintenance, réparation， panne'. La liste des types d'opération dépend fortement du modèle de machine.  - `operator`: Référence à l'opérateur qui effectue l'opération  - `owner`: Une liste contenant une séquence de caractères codés JSON référençant les identifiants uniques du ou des propriétaires.  - `plannedEndAt`: La date/heure de fin prévue pour l'opération. Notez qu'il s'agit d'un avis et que l'heure réelle de fin de l'opération peut être antérieure ou postérieure à la fin prévue.  - `plannedStartAt`: La date/heure de début prévue pour l'opération. Notez qu'il s'agit d'un avis et que l'heure réelle de début de l'opération peut être antérieure ou postérieure au début prévu.  - `result`: Le résultat de l'opération. L'un d'entre eux. Enum : 'ok, success, suspended, aborted, failed' (ok, succès, suspendu, interrompu, échoué)  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `startedAt`: Horodatage du début de l'exécution de l'opération.  - `status`: Un choix dans une liste énumérée décrivant l'état. L'un de ces choix. Enum : "planifié, en cours, terminé, programmé, annulé".  - `type`: Identifiant de l'entité NGSI. Il doit être ManufacturingMachineOperation.    
Propriétés requises  
- `id`  - `type`    
Ce modèle de données est issu du projet original GSMA IoT, https://www.gsma.com/iot/iot-big-data/. Il y a quelques adaptations mineures pour répondre aux exigences des modèles de données intelligents.  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ManufacturingMachineOperation:    
  description: 'A description of a Machine-Operation'    
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
    commandSequence:    
      description: 'The command sequence executed/ requested for the machine in a representation format relevant to the machine.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
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
    endedAt:    
      description: 'Timestamp when the operation actually finished.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &manufacturingmachineoperation_-_properties_-_owner_-_items_-_anyof    
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
    machine:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'A reference to the associated Machine for this machine operation.'    
      x-ngsi:    
        type: Relationship    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    operationOutput:    
      description: 'A custom property describing the output data of the operation. The properties of the schema of the output highly depends the machine model.'    
      properties:    
        faults:    
          type: number    
        unitsPrinted:    
          type: number    
      type: object    
      x-ngsi:    
        type: Property    
    operationType:    
      description: 'Defines the type of operation conducted/ requested. This will be one of a defined list of operation types specific to the machine/ machineModel.Including these. Enum:''process, setup，maintenance, repair，breakdown''. The list of operation types highly depends on the machine model.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    operator:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Reference to the operator conducting the operation'    
      x-ngsi:    
        type: Relationship    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *manufacturingmachineoperation_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    plannedEndAt:    
      description: 'The planned end date/timestamp for the operation. Note that this is advisory and the actual time the operation finishes may be before or after the planned end.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    plannedStartAt:    
      description: 'The planned start date/timestamp for the operation. Note that this is advisory and the actual time the operation starts may be before or after the planned start.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    result:    
      description: 'The result of the operation. One of these. Enum:''ok, success, suspended, aborted, failed'''    
      enum:    
        - aborted    
        - failed    
        - ok    
        - success    
        - suspended    
      type: string    
      x-ngsi:    
        type: Property    
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
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    startedAt:    
      description: 'Timestamp when the operation actually started to be performed.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    status:    
      description: 'A choice from an enumerated list describing the status. One of these. Enum:''planned, ongoing, finished, scheduled, cancelled'''    
      enum:    
        - cancelled    
        - finished    
        - ongoing    
        - planned    
        - scheduled    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity identifier. It has to be ManufacturingMachineOperation'    
      enum:    
        - ManufacturingMachineOperation    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.ManufacturingMachine/blob/master/ManufacturingMachineOperation/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.ManufacturingMachine/ManufacturingOperation/schema.json    
  x-model-tags: GSMA    
  x-version: 0.0.1    
```  
</details>    
## Exemples de charges utiles  
#### ManufacturingMachineOperation Valeurs-clés NGSI-v2 Exemple  
Voici un exemple d'une ManufacturingMachineOperation au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:MachineOperation:27577638-bd8a-4732-b418-fc8b949a0b0f",  
  "type": "ManufacturingMachineOperation",  
  "source": "https://source.example.com",  
  "dataProvider": "https://provider.example.com",  
  "machine": "urn:ngsi-ld:Machine:2033a7c7-d31b-48e7-91c2-014dc426c29e",  
  "operationType": [  
    "process"  
  ],  
  "description": "Printing of 1000 T-shirts",  
  "result": "ok",  
  "plannedStartAt": "2016-08-22T10:18:16Z",  
  "plannedEndAt": "2016-08-28T10:18:16Z",  
  "status": "finished",  
  "operator": "urn:ngsi-ld:Person:fd6f0070-47d7-11e8-a26c-0784612b9393",  
  "startedAt": "2016-08-22T10:18:16Z",  
  "endedAt": "2016-08-28T10:18:16Z",  
  "commandSequence": [  
    "Select inks",  
    "Prepare print masks",  
    "Print shirts",  
    "Clean print heads and rollers"  
  ],  
  "operationOutput": {  
    "Units Printed": 1000,  
    "Faults": 0  
  }  
}  
```  
#### ManufacturingMachineOperation NGSI-v2 normalisée Exemple  
Voici un exemple de ManufacturingMachineOperation au format JSON-LD tel que normalisé. Ceci est compatible avec NGSI-v2 lorsqu'on n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:MachineOperation:27577638-bd8a-4732-b418-fc8b949a0b0f",  
  "type": "ManufacturingMachineOperation",  
  "source": {  
    "type": "URL",  
    "value": "https://source.example.com"  
  },  
  "dataProvider": {  
    "type": "URL",  
    "value": "https://provider.example.com"  
  },  
  "machine": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:Machine:2033a7c7-d31b-48e7-91c2-014dc426c29e"  
  },  
  "operationType": {  
    "type": "array",  
    "value": [  
      "process"  
    ]  
  },  
  "description": {  
    "type": "Text",  
    "value": "Printing of 1000 T-shirts"  
  },  
  "result": {  
    "type": "Text",  
    "value": "ok"  
  },  
  "plannedStartAt": {  
    "type": "DateTime",  
    "value": "2016-08-22T10:18:16Z"  
  },  
  "plannedEndAt": {  
    "type": "DateTime",  
    "value": "2016-08-28T10:18:16Z"  
  },  
  "status": {  
    "type": "Text",  
    "value": "finished"  
  },  
  "operator": {  
    "type": "Relationship",  
    "value": "urn:ngsi-ld:Person:fd6f0070-47d7-11e8-a26c-0784612b9393"  
  },  
  "startedAt": {  
    "type": "DateTime",  
    "value": "2016-08-22T10:18:16Z"  
  },  
  "endedAt": {  
    "type": "DateTime",  
    "@value": "2016-08-28T10:18:16Z"  
  },  
  "commandSequence": {  
    "type": "array",  
    "value": [  
      "Select inks",  
      "Prepare print masks",  
      "Print shirts",  
      "Clean print heads and rollers"  
    ]  
  },  
  "operationOutput": {  
    "type": "StructuredValue",  
    "value": {  
      "Units Printed": 1000,  
      "Faults": 0  
    }  
  }  
}  
```  
#### ManufacturingMachineOperation Valeurs-clés NGSI-LD Exemple  
Voici un exemple de ManufacturingMachineOperation au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD quand on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.ManufacturingMachine/ManufacturingOperation/context.jsonld"  
  ],  
  "id": "urn:ngsi-ld:MachineOperation:27577638-bd8a-4732-b418-fc8b949a0b0f",  
  "type": "ManufacturingMachineOperation",  
  "source": "https://source.example.com",  
  "dataProvider": "https://provider.example.com",  
  "machine": "urn:ngsi-ld:Machine:2033a7c7-d31b-48e7-91c2-014dc426c29e",  
  "operationType": [  
    "process"  
  ],  
  "description": "Printing of 1000 T-shirts",  
  "result": "ok",  
  "plannedStartAt": "2016-08-22T10:18:16Z",  
  "plannedEndAt": "2016-08-28T10:18:16Z",  
  "status": "finished",  
  "operator": "urn:ngsi-ld:Person:fd6f0070-47d7-11e8-a26c-0784612b9393",  
  "startedAt": "2016-08-22T10:18:16Z",  
  "endedAt": "2016-08-28T10:18:16Z",  
  "commandSequence": [  
    "Select inks",  
    "Prepare print masks",  
    "Print shirts",  
    "Clean print heads and rollers"  
  ],  
  "operationOutput": {  
    "Units Printed": 1000,  
    "Faults": 0  
  }  
}  
```  
#### ManufacturingMachineOperation NGSI-LD normalisé Exemple  
Voici un exemple de ManufacturingMachineOperation au format JSON-LD tel que normalisé. Ce format est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "@context": [  
    "https://smart-data-models.github.io/dataModel.ManufacturingMachine/ManufacturingOperation/context.jsonld"  
  ],  
  "id": "urn:ngsi-ld:MachineOperation:27577638-bd8a-4732-b418-fc8b949a0b0f",  
  "type": "ManufacturingMachineOperation",  
  "source": {  
    "type": "Property",  
    "value": "https://source.example.com"  
  },  
  "dataProvider": {  
    "type": "Property",  
    "value": "https://provider.example.com"  
  },  
  "machine": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Machine:2033a7c7-d31b-48e7-91c2-014dc426c29e"  
  },  
  "operationType": {  
    "type": "Property",  
    "value": [  
      "process"  
    ]  
  },  
  "description": {  
    "type": "Property",  
    "value": "Printing of 1000 T-shirts"  
  },  
  "result": {  
    "type": "Property",  
    "value": "ok"  
  },  
  "plannedStartAt": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-08-22T10:18:16Z"  
    }  
  },  
  "plannedEndAt": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value": "2016-08-28T10:18:16Z"  
    }  
  },  
  "status": {  
    "type": "Property",  
    "value": "finished"  
  },  
  "operator": {  
    "type": "Relationship",  
    "object": "urn:ngsi-ld:Person:fd6f0070-47d7-11e8-a26c-0784612b9393"  
  },  
  "startedAt": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value":"2016-08-22T10:18:16Z"}  
  },  
  "endedAt": {  
    "type": "Property",  
    "value": {  
      "@type": "DateTime",  
      "@value":"2016-08-28T10:18:16Z"}  
  },  
  "commandSequence": {  
    "type": "Property",  
    "value": [  
      "Select inks",  
      "Prepare print masks",  
      "Print shirts",  
      "Clean print heads and rollers"  
    ]  
  },  
  "operationOutput": {  
    "type": "Property",  
    "value": {  
      "Units Printed": 1000,  
      "Faults": 0  
    }  
  }  
}  
```  
