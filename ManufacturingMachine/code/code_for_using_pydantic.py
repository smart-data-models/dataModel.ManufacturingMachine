from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import (
    AnyUrl,
    AwareDatetime,
    BaseModel,
    Field,
    RootModel,
    confloat,
    constr,
)


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


class InstallationNotes(BaseModel):
    docUri: Optional[AnyUrl] = None
    value: Optional[str] = None


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


class Type6(Enum):
    ManufacturingMachine = 'ManufacturingMachine'


class ManufacturingMachine(BaseModel):
    address: Optional[Address] = Field(None, description='The mailing address')
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    areaServed: Optional[str] = Field(
        None,
        description='The geographic area where a service or offered item is provided',
    )
    assetIdentifier: Optional[str] = Field(
        None,
        description='An asset identifier (e.g. asset tag number) assigned by the owner',
    )
    batteryLevel: Optional[confloat(ge=0.0, le=1.0)] = Field(
        None,
        description='Battery level. It must be equal to: 1.0 When the battery charge is full. 0.0 When the battery charge empty. Null when it cannot be determined',
    )
    building: Optional[
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
        description='Reference to the building entity instance into which this machine is installed',
    )
    countryOfManufacture: Optional[str] = Field(
        None, description='The country where this machine was manufactured'
    )
    current: Optional[float] = Field(
        None,
        description='The nominal required supply current (at the nominal supply voltage), in amps',
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
    factory: Optional[str] = Field(
        None, description='The factory name/code manufacturing this machine'
    )
    firmwareVersion: Optional[str] = Field(
        None, description='The (manufacturer specific) firmware version of this machine'
    )
    firstUsedAt: Optional[AwareDatetime] = Field(
        None,
        description='Indicates the date/time at which date and time the machine was first used (nominally in UTC)',
    )
    hardwareVersion: Optional[str] = Field(
        None, description='The (manufacturer specific) hardware version of this machine'
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
    installationNotes: Optional[InstallationNotes] = Field(
        None, description='Notes relating to this machine installation'
    )
    installedAt: Optional[AwareDatetime] = Field(
        None,
        description='Indicates the date/time at which date and time the machine was installed (nominally in UTC)',
    )
    location: Optional[
        Union[Location, Location1, Location2, Location3, Location4, Location5]
    ] = Field(
        None,
        description='Geojson reference to the item. It can be Point, LineString, Polygon, MultiPoint, MultiLineString or MultiPolygon',
    )
    machineModel: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(
        None, description='A reference to the associated Machine Model for this machine'
    )
    machineOwner: Optional[
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
        description='Reference to the owner or owners of the machine as either a Schema.org person or organization',
    )
    manufacturedAt: Optional[AwareDatetime] = Field(
        None,
        description='Indicates the date/time at which date and time the machine was manufactured (nominally in UTC)',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    online: Optional[bool] = Field(
        None,
        description='The communication status of this machine. A logical representation of Offline (false) or Online (true)',
    )
    osVersion: Optional[str] = Field(
        None,
        description='The (manufacturer specific) operating system version of this machine',
    )
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
    power: Optional[float] = Field(
        None, description='The nominal rated power consumption of the machine in kW'
    )
    rotationalSpeed: Optional[float] = Field(
        None,
        description=' \\tThe maximum rotational speed in rpm (for machines such as drills, lathes)',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    serialNumber: Optional[str] = Field(
        None, description='The serial number assigned by the manufacturer'
    )
    softwareVersion: Optional[str] = Field(
        None, description='The (manufacturer specific) software version of this machine'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    status: Optional[str] = Field(
        None,
        description='Text formatted (current) machine status code or description. Expected to be the manufacturer or machine specific status code generated by the machine',
    )
    subscriptionService: Optional[
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
        description='Reference to service subscriptions related to this machine e.g. energy supplies, Internet Service Providers etc, maintenance',
    )
    supplierName: Optional[str] = Field(
        None, description='The name of the supplier of this machine'
    )
    supportedProtocol: Optional[List[str]] = Field(
        None, description='Supported protocol(s) or networks'
    )
    type: Optional[Type6] = Field(
        None, description='NGSI entity type. It has to be ManufacturingMachine'
    )
    voltage: Optional[float] = Field(
        None, description='The nominal required supply voltage, in volts'
    )
