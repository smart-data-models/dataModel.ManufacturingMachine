<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティ製造機械  
==========<!-- /10-Header -->  
<!-- 15-License -->  
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.ManufacturingMachine/blob/master/ManufacturingMachine/LICENSE.md)  
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな説明**一般的なマシンの説明**。  
バージョン: 0.0.1  
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
- `alternateName[string]`: この項目の別名  - `areaServed[string]`: サービスまたは提供品が提供される地理的地域  . Model: [https://schema.org/Text](https://schema.org/Text)- `assetIdentifier[string]`: 所有者によって割り当てられた資産識別子（資産タグ番号など  . Model: [https://schema.org/Text](https://schema.org/Text)- `batteryLevel[number]`: バッテリー残量。と等しくなければならない：1.0 バッテリーが満充電のとき。0.0 バッテリー充電が空のとき。判断できない場合はNULL  . Model: [https://schema.org/Number](https://schema.org/Number)- `building[*]`: このマシンがインストールされているビルディング・エンティティのインスタンスへの参照  - `countryOfManufacture[string]`: このマシンが製造された国  . Model: [https://schema.org/Text](https://schema.org/Text)- `current[number]`: 公称必要電源電流（公称電源電圧時）、単位：アンペア  . Model: [https://schema.org/Number](https://schema.org/Number)- `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `factory[string]`: このマシンを製造している工場名/コード  . Model: [https://schema.org/Text](https://schema.org/Text)- `firmwareVersion[string]`: 本機の（メーカー固有の）ファームウェア・バージョン  . Model: [https://schema.org/Text](https://schema.org/Text)- `firstUsedAt[date-time]`: マシンが最初に使用された日付/時刻を示す（公称はUTC）。  . Model: [https://schema.org/Text](https://schema.org/Text)- `hardwareVersion[string]`: このマシンの（メーカー固有の）ハードウェア・バージョン  . Model: [https://schema.org/Text](https://schema.org/Text)- `id[*]`: エンティティの一意識別子  - `installationNotes[object]`: 本機の設置に関する注意事項  . Model: [https://schema.org/Text](https://schema.org/Text)	- `docUri`:     
- `installedAt[date-time]`: マシンがインストールされた日付/時刻を示す（公称UTC）。  . Model: [https://schema.org/Text](https://schema.org/Text)- `location[*]`: アイテムへの Geojson 参照。Point、LineString、Polygon、MultiPoint、MultiLineString、MultiPolygon のいずれか。  - `machineModel[*]`: このマシンの関連するマシンモデルへの参照  - `machineOwner[array]`: Schema.orgの個人または組織として、マシンの所有者または所有者への言及  - `manufacturedAt[date-time]`: マシンが製造された日付/時刻を示す（公称は UTC）。  . Model: [https://schema.org/Text](https://schema.org/Text)- `name[string]`: このアイテムの名前  - `online[boolean]`: このマシンの通信状態。Offline(false)またはOnline(true)の論理表現。  . Model: [https://schema.org/Boolean](https://schema.org/Boolean)- `osVersion[string]`: このマシンの（メーカー固有の）オペレーティング・システムのバージョン  . Model: [https://schema.org/Text](https://schema.org/Text)- `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `power[number]`: 機械の公称定格消費電力（kW  . Model: [https://schema.org/Number](https://schema.org/Number)- `rotationalSpeed[number]`:  	最高回転速度（rpm）（ドリル、旋盤などの機械用  . Model: [https://schema.org/Number](https://schema.org/Number)- `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `serialNumber[string]`: 製造者によって割り当てられたシリアル番号  . Model: [https://schema.org/Text](https://schema.org/Text)- `softwareVersion[string]`: 本機の（メーカー固有の）ソフトウェア・バージョン  . Model: [https://schema.org/Text](https://schema.org/Text)- `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `status[string]`: テキスト形式の（現在の）機械ステータスコードまたは説明。マシンによって生成される製造業者またはマシン固有のステータスコードであることが期待される。  . Model: [https://schema.org/Text](https://schema.org/Text)- `subscriptionService[array]`: 本機に関連するサービス契約（エネルギー供給、インターネット・サービス・プロバイダーなど）、メンテナンスへの言及。  - `supplierName[string]`: 本機のサプライヤー名  . Model: [https://schema.org/Text](https://schema.org/Text)- `supportedProtocol[array]`: 対応プロトコルまたはネットワーク  . Model: [https://schema.org/Text](https://schema.org/Text)- `type[string]`: NGSI エンティティタイプ。ManufacturingMachineでなければならない。  - `voltage[number]`: 公称必要電源電圧（単位：ボルト  . Model: [https://schema.org/Number](https://schema.org/Number)<!-- /30-PropertiesList -->  
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
ManufacturingMachine:    
  description: Description of a generic machine    
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
    assetIdentifier:    
      description: An asset identifier (e.g. asset tag number) assigned by the owner    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    batteryLevel:    
      description: 'Battery level. It must be equal to: 1.0 When the battery charge is full. 0.0 When the battery charge empty. Null when it cannot be determined'    
      maximum: 1    
      minimum: 0    
      type: number    
      x-ngsi:    
        model: https://schema.org/Number    
        type: Property    
    building:    
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
      description: Reference to the building entity instance into which this machine is installed    
      x-ngsi:    
        type: Relationship    
    countryOfManufacture:    
      description: The country where this machine was manufactured    
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
    factory:    
      description: The factory name/code manufacturing this machine    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    firmwareVersion:    
      description: The (manufacturer specific) firmware version of this machine    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    firstUsedAt:    
      description: Indicates the date/time at which date and time the machine was first used (nominally in UTC)    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    hardwareVersion:    
      description: The (manufacturer specific) hardware version of this machine    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    installationNotes:    
      description: Notes relating to this machine installation    
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
      description: Indicates the date/time at which date and time the machine was installed (nominally in UTC)    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    machineModel:    
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
      description: A reference to the associated Machine Model for this machine    
      x-ngsi:    
        type: Relationship    
    machineOwner:    
      description: Reference to the owner or owners of the machine as either a Schema.org person or organization    
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
    manufacturedAt:    
      description: Indicates the date/time at which date and time the machine was manufactured (nominally in UTC)    
      format: date-time    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    name:    
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    online:    
      description: The communication status of this machine. A logical representation of Offline (false) or Online (true)    
      type: boolean    
      x-ngsi:    
        model: https://schema.org/Boolean    
        type: Property    
    osVersion:    
      description: The (manufacturer specific) operating system version of this machine    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
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
    power:    
      description: The nominal rated power consumption of the machine in kW    
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
    serialNumber:    
      description: The serial number assigned by the manufacturer    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    softwareVersion:    
      description: The (manufacturer specific) software version of this machine    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    status:    
      description: Text formatted (current) machine status code or description. Expected to be the manufacturer or machine specific status code generated by the machine    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    subscriptionService:    
      description: 'Reference to service subscriptions related to this machine e.g. energy supplies, Internet Service Providers etc, maintenance'    
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
    supplierName:    
      description: The name of the supplier of this machine    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    supportedProtocol:    
      description: Supported protocol(s) or networks    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    type:    
      description: NGSI entity type. It has to be ManufacturingMachine    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
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
## ペイロードの例  
#### ManufacturingMachine NGSI-v2 キー値の例  
以下は、ManufacturingMachineをJSON-LD形式でkey-valuesとした例である。これはNGSI-v2と互換性があり、`options=keyValues`を使用すると、個々のエンティティのコンテキストデータを返す。  
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
#### ManufacturingMachine NGSI-v2 正規化例  
以下は、正規化された JSON-LD 形式の ManufacturingMachine の例である。これは、オプションを使用しない場合、NGSI-v2と互換性があり、個々のエンティティのコンテキスト・データを返します。  
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
#### ManufacturingMachine NGSI-LD キー値の例  
JSON-LD形式のManufacturingMachineをkey-valuesとした例である。これは NGSI-LD と互換性があり、`options=keyValues` を使うと個々のエンティティのコンテキストデータを返す。  
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
#### ManufacturingMachine NGSI-LD 正規化例  
以下は、正規化された JSON-LD 形式の ManufacturingMachine の例である。これは、オプションを使用しない場合の NGSI-LD と互換性があり、個々のエンティティのコンテキスト・データを返します。  
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
        "type": "GeoProperty",  
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
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
