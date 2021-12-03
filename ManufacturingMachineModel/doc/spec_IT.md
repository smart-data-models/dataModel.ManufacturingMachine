Entità: ManufacturingMachineModel  
=================================  
[Licenza aperta](https://github.com/smart-data-models//dataModel.ManufacturingMachine/blob/master/ManufacturingMachineModel/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descrizione globale: **Questa entità contiene una descrizione armonizzata di un modello generico di macchina. Questa entità è principalmente associata al segmento industriale e alle relative applicazioni IoT. Il machineModel include una struttura gerarchica che permette ai modelli di macchina di essere raggruppati in modo flessibile.**  

## Elenco delle proprietà  

- `address`: L'indirizzo postale  - `alternateName`: Un nome alternativo per questa voce  - `areaServed`: L'area geografica in cui viene fornito un servizio o un articolo offerto  - `brandName`: Il nome della marca di questa macchinaModello.  - `dataProvider`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated`: Timestamp di creazione dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `dateModified`: Timestamp dell'ultima modifica dell'entità. Questo sarà di solito assegnato dalla piattaforma di archiviazione.  - `description`: Una descrizione di questo articolo  - `documentation`: Riferimento alla scheda tecnica o altra documentazione del produttore su questo modello di macchina.  - `id`: Identificatore unico dell'entità  - `location`: Riferimento Geojson all'elemento. Può essere Point, LineString, Polygon, MultiPoint, MultiLineString o MultiPolygon  - `machineModelChildren`: Fa riferimento a qualsiasi entità MachineModel di livello inferiore che si basa su questo modello di macchina.  - `machineModelParent`: Fa riferimento a qualsiasi MachineModel di livello superiore su cui si basa questo modello di macchina.  - `manufacturerName`: Il nome del produttore di questa macchinaModello.  - `manufacturingMachineType`: Una lista di categorie funzionali che questo modello di macchina supporta. Enum:'robot, cnc, 2dPrinter, 3dPrinter, 3dScanner, tornio, injectionMolding, laserCutter, millingMachine, grindingMachine, stampingMachine, oven, kiln, packaging, mixer, dryer, fan, saw'  - `name`: Il nome di questo articolo.  - `owner`: Una lista contenente una sequenza di caratteri codificata in JSON che si riferisce agli ID unici dei proprietari  - `processDescription`: Una descrizione del processo industriale realizzato da questa macchina.  - `root`: Un indicatore logico che questo modello di macchina di produzione è la radice di una gerarchia di modelli di macchina: True indica che è la radice, false indica che non è la radice.  - `seeAlso`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source`: Una sequenza di caratteri che dà la fonte originale dei dati dell'entità come URL. Si raccomanda di essere il nome di dominio completamente qualificato del fornitore di origine, o l'URL dell'oggetto di origine.  - `standardOperations`: Elenca l'insieme standard di operazioni supportate da questo machineModel.  - `type`: Identificatore di entità NGSI. Deve essere ManufacturingMachineModel  - `version`: Il numero di versione definito dal produttore per il modello di macchina.    
Proprietà richieste  
- `id`  - `type`    
Questo modello di dati proviene dal progetto originale GSMA IoT, https://www.gsma.com/iot/iot-big-data/. Ci sono alcuni adattamenti minori per soddisfare i requisiti dei modelli di dati intelligenti.  
## Descrizione del modello di dati delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ManufacturingMachineModel:    
  description: 'This entity contains a harmonised description of a generic machine model. This entity is primarily associated with the industry segment and related IoT applications. The machineModel includes a hierarchical structure that allows machine models to be grouped in a flexible way.'    
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
    brandName:    
      description: 'The brand name of this MachineModel.'    
      type: string    
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
    documentation:    
      description: 'Reference to data sheet or other manufacturer’s documentation about this MachineModel.'    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &manufacturingmachinemodel_-_properties_-_owner_-_items_-_anyof    
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
    machineModelChildren:    
      description: 'References any lower level MachineModel entities that are based on this machine model.'    
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
    machineModelParent:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'References any higher level MachineModel that this machine model is based on.'    
      x-ngsi:    
        type: Relationship    
    manufacturerName:    
      description: 'The name of manufacturer of this MachineModel.'    
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
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *manufacturingmachinemodel_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    processDescription:    
      description: 'A description of the industrial process carried out by this machine.'    
      type: string    
      x-ngsi:    
        type: Property    
    root:    
      description: 'A logical indicator that this Manufacturing Machine Model is the root of a Machine Model hierarchy.True indicates it is the root, false indicates that it is not the root.'    
      type: boolean    
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
    standardOperations:    
      description: 'Lists the standard set of operations supported by this machineModel.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI Entity identifier. It has to be ManufacturingMachineModel'    
      enum:    
        - ManufacturingMachineModel    
      type: string    
      x-ngsi:    
        type: Property    
    version:    
      description: 'The manufacturer defined version number for the machine model.'    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.ManufacturingMachine/blob/master/ManufacturingMachineModel/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.ManufacturingMachine/ManufacturingMachineModel/schema.json    
  x-model-tags: GSMA    
  x-version: 0.0.1    
```  
</details>    
## Esempio di payloads  
#### ManufacturingMachineModel NGSI-v2 valori chiave Esempio  
Ecco un esempio di un ManufacturingMachineModel in formato JSON-LD come valori chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
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
#### ManufacturingMachineModel NGSI-v2 normalizzato Esempio  
Ecco un esempio di un ManufacturingMachineModel in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
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
#### ManufacturingMachineModel Valori chiave NGSI-LD Esempio  
Ecco un esempio di un ManufacturingMachineModel in formato JSON-LD come key-values. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.github.io/dataModel.Transportation/context.jsonld"  
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
#### ManufacturingMachineModel NGSI-LD normalizzato Esempio  
Ecco un esempio di un ManufacturingMachineModel in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non usa opzioni e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "@context": [  
    "https://smartdatamodels.github.io/dataModel.Transportation/context.jsonld"  
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
    "value":  "https://example.com"  
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
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per avere una risposta su come trattare le unità di grandezza