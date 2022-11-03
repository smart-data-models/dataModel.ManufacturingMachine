<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体。制造机器模型  
=========<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.ManufacturingMachine/blob/master/ManufacturingMachineModel/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述。**该实体包含一个通用机器模型的统一描述。该实体主要与行业领域和相关的物联网应用有关。machineModel包括一个分层结构，允许机器模型以灵活的方式进行分组。  
版本：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `address[object]`: 邮寄地址  . Model: [https://schema.org/address](https://schema.org/address)- `alternateName[string]`: 这个项目的一个替代名称  - `areaServed[string]`: 提供服务或提供项目的地理区域  . Model: [https://schema.org/Text](https://schema.org/Text)- `brandName[string]`: 该机器的品牌名称Model。  - `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `description[string]`: 对这个项目的描述  - `documentation[string]`: 参考数据表或其他制造商关于该机器模型的文件。  - `id[*]`: 实体的唯一标识符  - `location[*]`: 对该项目的Geojson引用。它可以是点、线字符串、多边形、多点、多线字符串或多多边形。  - `machineModelChildren[array]`: 引用基于此机器模型的任何低级别的MachineModel实体。  - `machineModelParent[*]`: 引用该机器模型所基于的任何更高级别的MachineModel。  - `manufacturerName[string]`: 该机器的制造商名称Model。  - `manufacturingMachineType[array]`: 该机器模型支持的功能类别的列表。Enum:'机器人, cnc, 2dPrinter, 3dPrinter, 3dScanner, lathe, injectionMolding, laserCutter, millingMachine, grindingMachine, stampingMachine, oven, kiln, packaging, mixer, dryer, fan, saw' 。  - `name[string]`: 这个项目的名称。  - `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `processDescription[string]`: 对这台机器所进行的工业流程的描述。  - `root[boolean]`: 一个逻辑指标，表明这个制造机器模型是机器模型层次结构的根。真表示它是根，假表示它不是根。  - `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `source[string]`: 一系列的字符，以URL的形式给出实体数据的原始来源。建议为源提供者的完全合格域名，或源对象的URL。  - `standardOperations[array]`: 列出这个machineModel所支持的标准操作集。  - `type[string]`: NGSI实体标识符。它必须是ManufacturingMachineModel。  - `version[string]`: 制造商为机器型号定义的版本号。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
这个数据模型来自原始项目GSMA物联网项目，https://www.gsma.com/iot/iot-big-data/。有一些小的调整，以满足智能数据模型的要求。  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 数据模型的属性描述  
按字母顺序排列（点击查看详情）。  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
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
        - description: 'GeoProperty. Geojson reference to the item. Point'    
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
        - description: 'GeoProperty. Geojson reference to the item. LineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. Polygon'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiPoint'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        - description: 'GeoProperty. Geojson reference to the item. MultiLineString'    
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
        type: GeoProperty    
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
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ＃＃＃＃有效载荷的例子  
#### ManufacturingMachineModel NGSI-v2 key-values 示例  
这里是一个以JSON-LD格式作为key-values的ManufacturingMachineModel的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
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
#### ManufacturingMachineModel NGSI-v2规范化示例  
下面是一个以JSON-LD格式规范化的ManufacturingMachineModel的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
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
#### ManufacturingMachineModel NGSI-LD key-values 示例  
这里是一个以JSON-LD格式作为key-values的ManufacturingMachineModel的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
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
#### ManufacturingMachineModel NGSI-LD规范化实例  
下面是一个JSON-LD格式的ManufacturingMachineModel规范化的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
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
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
