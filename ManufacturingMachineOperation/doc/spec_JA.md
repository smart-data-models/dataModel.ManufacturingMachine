<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
エンティティ製造機械操作    
============<!-- /10-Header -->    
<!-- 15-License -->    
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.ManufacturingMachine/blob/master/ManufacturingMachineOperation/LICENSE.md)    
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
グローバルな記述：**このエンティティには、一般的な機械操作の調和された記述が含まれる。このエンティティは、主に産業セグメントと関連する IoT アプリケーションに関連する。各 MachineOperation インスタンスは、特定の Machine インスタンスに関連する。    
バージョン: 0.0.2    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## プロパティのリスト    
<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。    
- `address[object]`: 郵送先住所  . Model: [https://schema.org/address](https://schema.org/address)	- `addressCountry[string]`: 国。例えば、スペイン  . Model: [https://schema.org/addressCountry](https://schema.org/addressCountry)    
	- `addressLocality[string]`: 番地がある地域と、その地域に含まれる地域  . Model: [https://schema.org/addressLocality](https://schema.org/addressLocality)    
	- `addressRegion[string]`: その地域がある地域、またその国がある地域  . Model: [https://schema.org/addressRegion](https://schema.org/addressRegion)    
	- `district[string]`: 地区とは行政区画の一種で、国によっては地方自治体によって管理されている。      
	- `postOfficeBoxNumber[string]`: 私書箱の住所のための私書箱番号。例：03578  . Model: [https://schema.org/postOfficeBoxNumber](https://schema.org/postOfficeBoxNumber)    
	- `postalCode[string]`: 郵便番号。例：24004  . Model: [https://schema.org/https://schema.org/postalCode](https://schema.org/https://schema.org/postalCode)    
	- `streetAddress[string]`: 番地  . Model: [https://schema.org/streetAddress](https://schema.org/streetAddress)    
- `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `commandSequence[array]`: マシンに関連する表現フォーマットで、マシンに対して実行/要求されたコマンドシーケンス  - `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `endedAt[date-time]`: 操作が実際に終了したタイムスタンプ  - `id[*]`: エンティティの一意識別子  - `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `machine[*]`: このマシン操作に関連するマシンへの参照。  - `name[string]`: このアイテムの名前  - `operationOutput[object]`: 操作の出力データを記述するカスタムプロパティ。出力のスキーマのプロパティは、マシンモデルに大きく依存します。  	- `faults`:       
- `operationType[array]`: 実施/要求される操作のタイプを定義する。これは、機械/機械モデルに固有の操作タイプの定義されたリストの1つになります。列挙：「プロセス，セットアップ，メンテナンス，修理，故障」。操作タイプのリストは、機械モデルに大きく依存します。  - `operator[*]`: 運航を実施するオペレーターに関する言及  - `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `plannedEndAt[date-time]`: 操作の終了予定日/タイムスタンプ。これは助言的なものであり、実際の操作の終了時刻は計画された終了時刻の前後になる可能性があることに注意。  - `plannedStartAt[date-time]`: 予定されている操作の開始日/タイムスタンプ。これは助言的なものであり、実際の操作開始時刻は計画された開始時刻の前後になる可能性があることに注意してください。  - `result[string]`: 手術の結果以下のいずれか。Enum:'OK、成功、中断、中止、失敗'  - `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `startedAt[date-time]`: 実際に操作が開始されたタイムスタンプ  - `status[string]`: ステータスを表す列挙リストからの選択。以下のいずれか。列挙:'計画中、進行中、終了、予定、キャンセル'  - `type[string]`: NGSI エンティティ識別子。これは ManufacturingMachineOperation でなければならない。  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
必須プロパティ    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
このデータ・モデルはGSMA IoTプロジェクト（https://www.gsma.com/iot/iot-big-data/）に由来する。スマート・データ・モデルの要件を満たすために、若干の修正が加えられている。    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## プロパティのデータモデル記述    
アルファベット順（クリックで詳細表示）    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
ManufacturingMachineOperation:      
  description: This entity contains a harmonised description of a generic machine operation. This entity is primarily associated with the industry segment and related IoT applications. Each MachineOperation instance will be related to a specific Machine instance.      
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
    commandSequence:      
      description: The command sequence executed/ requested for the machine in a representation format relevant to the machine      
      items:      
        type: string      
      type: array      
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
    endedAt:      
      description: Timestamp when the operation actually finished      
      format: date-time      
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
    machine:      
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
      description: A reference to the associated Machine for this machine operation      
      x-ngsi:      
        type: Relationship      
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    operationOutput:      
      description: A custom property describing the output data of the operation. The properties of the schema of the output highly depends the machine model      
      properties:      
        faults:      
          type: number      
        unitsPrinted:      
          type: number      
      type: object      
      x-ngsi:      
        type: Property      
    operationType:      
      description: 'Defines the type of operation conducted/ requested. This will be one of a defined list of operation types specific to the machine/ machineModel.Including these. Enum:''process, setup，maintenance, repair，breakdown''. The list of operation types highly depends on the machine model'      
      items:      
        type: string      
      type: array      
      x-ngsi:      
        type: Property      
    operator:      
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
      description: Reference to the operator conducting the operation      
      x-ngsi:      
        type: Relationship      
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
    plannedEndAt:      
      description: The planned end date/timestamp for the operation. Note that this is advisory and the actual time the operation finishes may be before or after the planned end      
      format: date-time      
      type: string      
      x-ngsi:      
        type: Property      
    plannedStartAt:      
      description: The planned start date/timestamp for the operation. Note that this is advisory and the actual time the operation starts may be before or after the planned start      
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
    startedAt:      
      description: Timestamp when the operation actually started to be performed      
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
      description: NGSI Entity identifier. It has to be ManufacturingMachineOperation      
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
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
## ペイロードの例    
#### ManufacturingMachineOperation NGSI-v2 キー値の例    
以下は、ManufacturingMachineOperationをJSON-LD形式でkey-valuesとした例である。これは NGSI-v2 と互換性があり、`options=keyValues` を使用すると個々のエンティティのコンテキストデータを返す。    
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
#### ManufacturingMachineOperation NGSI-v2 正規化例    
以下は、正規化されたJSON-LD形式のManufacturingMachineOperationの例である。これは、オプションを使用しない場合は NGSI-v2 と互換性があり、個々のエンティティのコンテキスト・データを返します。    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:MachineOperation:27577638-bd8a-4732-b418-fc8b949a0b0f",  
  "type": "ManufacturingMachineOperation",  
  "source": {  
    "type": "Text",  
    "value": "https://source.example.com"  
  },  
  "dataProvider": {  
    "type": "Text",  
    "value": "https://provider.example.com"  
  },  
  "machine": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:Machine:2033a7c7-d31b-48e7-91c2-014dc426c29e"  
  },  
  "operationType": {  
    "type": "StructuredValue",  
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
    "type": "Text",  
    "value": "urn:ngsi-ld:Person:fd6f0070-47d7-11e8-a26c-0784612b9393"  
  },  
  "startedAt": {  
    "type": "DateTime",  
    "value": "2016-08-22T10:18:16Z"  
  },  
  "endedAt": {  
    "type": "DateTime",  
    "value": "2016-08-28T10:18:16Z"  
  },  
  "commandSequence": {  
    "type": "StructuredValue",  
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
#### ManufacturingMachineOperation NGSI-LD キー値の例    
以下は、ManufacturingMachineOperationをJSON-LD形式でkey-valuesとした例である。これは NGSI-LD と互換性があり、`options=keyValues` を使うと個々のエンティティのコンテキストデータを返す。    
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
#### ManufacturingMachineOperation NGSI-LD 正規化例    
以下は、正規化された JSON-LD 形式の ManufacturingMachineOperation の例である。これは、オプションを使用しない場合の NGSI-LD と互換性があり、個々のエンティティのコンテキスト・データを返します。    
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
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
