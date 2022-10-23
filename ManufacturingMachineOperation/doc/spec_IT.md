<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: ManufacturingMachineOperation  
=====================================<!-- /10-Header -->  
<!-- 15-License -->  
[Licenza aperta](https://github.com/smart-data-models//dataModel.ManufacturingMachine/blob/master/ManufacturingMachineOperation/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Descrizione globale: **Questa entità contiene una descrizione armonizzata di una generica operazione della macchina. Questa entità è associata principalmente al segmento industriale e alle relative applicazioni IoT. Ogni istanza di MachineOperation sarà correlata a una specifica istanza di Macchina.**  
versione: 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Elenco delle proprietà  

<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.  
- `address[object]`: L'indirizzo postale  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: Un nome alternativo per questa voce  - `areaServed[string]`: L'area geografica in cui viene fornito il servizio o l'articolo offerto.  . Model: [https://schema.org/Text](https://schema.org/Text)- `commandSequence[array]`: La sequenza di comandi eseguita/richiesta per la macchina in un formato di rappresentazione pertinente alla macchina.  - `dataProvider[string]`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated[string]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `dateModified[string]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `description[string]`: Descrizione dell'articolo  - `endedAt[string]`: Timestamp del momento in cui l'operazione è effettivamente terminata.  - `id[*]`: Identificatore univoco dell'entità  - `location[*]`: Riferimento Geojson all'elemento. Può essere un punto, una stringa di linea, un poligono, un multi-punto, una stringa di linea o un poligono multiplo.  - `machine[*]`: Un riferimento alla macchina associata per questa operazione della macchina.  - `name[string]`: Il nome di questo elemento.  - `operationOutput[object]`: Una proprietà personalizzata che descrive i dati di output dell'operazione. Le proprietà dello schema dell'output dipendono fortemente dal modello di macchina.  - `operationType[array]`: Definisce il tipo di operazione condotta/richiesta. Sarà uno di un elenco definito di tipi di operazione specifici per la macchina/modello di macchina. Enum:'processo, impostazione, manutenzione, riparazione, guasto'. L'elenco dei tipi di operazione dipende fortemente dal modello di macchina.  - `operator[*]`: Riferimento all'operatore che conduce l'operazione  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `plannedEndAt[string]`: La data/ora di fine prevista per l'operazione. Si noti che si tratta di un dato consultivo e che l'ora effettiva in cui l'operazione termina può essere precedente o successiva al termine previsto.  - `plannedStartAt[string]`: La data/ora di inizio prevista per l'operazione. Si noti che si tratta di un'indicazione consultiva e che l'ora effettiva di inizio dell'operazione può essere precedente o successiva a quella pianificata.  - `result[string]`: Il risultato dell'operazione. Uno di questi. Enum:'ok, successo, sospeso, interrotto, fallito'.  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `startedAt[string]`: Timestamp del momento in cui l'operazione ha iniziato a essere eseguita.  - `status[string]`: Una scelta da un elenco enumerato che descrive lo stato. Uno di questi. Enum:'pianificato, in corso, finito, programmato, annullato'.  - `type[string]`: Identificatore dell'entità NGSI. Deve essere ManufacturingMachineOperation.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Proprietà richieste  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
Questo modello di dati proviene dal progetto originale GSMA IoT, https://www.gsma.com/iot/iot-big-data/. Sono stati apportati alcuni piccoli adattamenti per soddisfare i requisiti dei modelli di dati intelligenti.  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
ManufacturingMachineOperation:    
  description: 'This entity contains a harmonised description of a generic machine operation. This entity is primarily associated with the industry segment and related IoT applications. Each MachineOperation instance will be related to a specific Machine instance.'    
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
  x-model-schema: https://smart-data-models.github.io/dataModel.ManufacturingMachine/ManufacturingMachineOperation/schema.json    
  x-model-tags: GSMA    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Esempi di payload  
#### ManufacturingMachineOperation Valori chiave NGSI-v2 Esempio  
Ecco un esempio di ManufacturingMachineOperation in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### ManufacturingMachineOperation NGSI-v2 normalizzato Esempio  
Ecco un esempio di ManufacturingMachineOperation in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### ManufacturingMachineOperation Valori-chiave NGSI-LD Esempio  
Ecco un esempio di ManufacturingMachineOperation in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "@context": [  
        "https://smart-data-models.github.io/dataModel.ManufacturingMachine/ManufacturingOperation/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.ManufacturingMachine/master/context.jsonld"  
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
</details>  
#### ManufacturingMachineOperation NGSI-LD normalizzato Esempio  
Ecco un esempio di ManufacturingMachineOperation in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "@context": [  
        "https://smart-data-models.github.io/dataModel.ManufacturingMachine/ManufacturingOperation/context.jsonld",  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.ManufacturingMachine/master/context.jsonld"  
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
            "@value": "2016-08-22T10:18:16Z"  
        }  
    },  
    "endedAt": {  
        "type": "Property",  
        "value": {  
            "@type": "DateTime",  
            "@value": "2016-08-28T10:18:16Z"  
        }  
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
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
