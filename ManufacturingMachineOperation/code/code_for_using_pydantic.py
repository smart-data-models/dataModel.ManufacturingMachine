from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, RootModel, constr


class Address(BaseModel):
    addressCountry: Optional[str] = Field(
        None, description='The country. For example, Spain'
    )
    addressLocality: Optional[str] = Field(
        None,
        description='The locality in which the street address is, and which is in the region',
    )
    addressRegion: Optional[str] = Field(
        None,
        description='The region in which the locality is, and which is in the country',
    )
    district: Optional[str] = Field(
        None,
        description='A district is a type of administrative division that, in some countries, is managed by the local government',
    )
    postOfficeBoxNumber: Optional[str] = Field(
        None,
        description='The post office box number for PO box addresses. For example, 03578',
    )
    postalCode: Optional[str] = Field(
        None, description='The postal code. For example, 24004'
    )
    streetAddress: Optional[str] = Field(None, description='The street address')
    streetNr: Optional[str] = Field(
        None, description='Number identifying a specific property on a public street'
    )


class Type(Enum):
    Point = 'Point'


class Location(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[float] = Field(..., min_length=2)
    type: Type


class Coordinate(RootModel[List[float]]):
    root: List[float]


class Type1(Enum):
    LineString = 'LineString'


class Location1(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[Coordinate] = Field(..., min_length=2)
    type: Type1


class Type2(Enum):
    Polygon = 'Polygon'


class Location2(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type2


class Type3(Enum):
    MultiPoint = 'MultiPoint'


class Location3(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[float]]
    type: Type3


class Type4(Enum):
    MultiLineString = 'MultiLineString'


class Location4(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[Coordinate]]
    type: Type4


class Type5(Enum):
    MultiPolygon = 'MultiPolygon'


class Location5(BaseModel):
    bbox: Optional[List[float]] = Field(None, min_length=4)
    coordinates: List[List[List[Coordinate]]]
    type: Type5


class OperationOutput(BaseModel):
    faults: Optional[float] = None
    unitsPrinted: Optional[float] = None


class Result(Enum):
    aborted = 'aborted'
    failed = 'failed'
    ok = 'ok'
    success = 'success'
    suspended = 'suspended'


class Status(Enum):
    cancelled = 'cancelled'
    finished = 'finished'
    ongoing = 'ongoing'
    planned = 'planned'
    scheduled = 'scheduled'


class Type6(Enum):
    ManufacturingMachineOperation = 'ManufacturingMachineOperation'


class ManufacturingMachineOperation(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    commandSequence: Optional[List[str]] = Field(
        None,
        description='The command sequence executed/ requested for the machine in a representation format relevant to the machine',
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    endedAt: Optional[AwareDatetime] = Field(
        None, description='Timestamp when the operation actually finished'
    )
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    machine: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(
        None,
        description='A reference to the associated Machine for this machine operation',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    operationOutput: Optional[OperationOutput] = Field(
        None,
        description='A custom property describing the output data of the operation. The properties of the schema of the output highly depends the machine model',
    )
    operationType: Optional[List[str]] = Field(
        None,
        description="Defines the type of operation conducted/ requested. This will be one of a defined list of operation types specific to the machine/ machineModel.Including these. Enum:'process, setup，maintenance, repair，breakdown'. The list of operation types highly depends on the machine model",
    )
    operator: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Reference to the operator conducting the operation')
    owner: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)',
    )
    plannedEndAt: Optional[AwareDatetime] = Field(
        None,
        description='The planned end date/timestamp for the operation. Note that this is advisory and the actual time the operation finishes may be before or after the planned end',
    )
    plannedStartAt: Optional[AwareDatetime] = Field(
        None,
        description='The planned start date/timestamp for the operation. Note that this is advisory and the actual time the operation starts may be before or after the planned start',
    )
    result: Optional[Result] = Field(
        None,
        description="The result of the operation. One of these. Enum:'ok, success, suspended, aborted, failed'",
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    startedAt: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp when the operation actually started to be performed',
    )
    status: Optional[Status] = Field(
        None,
        description="A choice from an enumerated list describing the status. One of these. Enum:'planned, ongoing, finished, scheduled, cancelled'",
    )
    type: Optional[Type6] = Field(
        None,
        description='NGSI Entity identifier. It has to be ManufacturingMachineOperation',
    )
