/* (Beta) Export of data model ManufacturingMachine of the subject dataModel.ManufacturingMachine for a postgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE ManufacturingMachine_type AS ENUM ('ManufacturingMachine');
CREATE TABLE ManufacturingMachine (address json, alternateName text, areaServed text, assetIdentifier text, batteryLevel text, building text, countryOfManufacture text, current text, dataProvider text, dateCreated timestamp, dateModified timestamp, description text, factory text, firmwareVersion text, firstUsedAt timestamp, hardwareVersion text, id text, installationNotes json, installedAt timestamp, location json, machineModel text, machineOwner json, manufacturedAt timestamp, name text, online text, osVersion text, owner json, power text, rotationalSpeed text, seeAlso json, serialNumber text, softwareVersion text, source text, status text, subscriptionService json, supplierName text, supportedProtocol json, type ManufacturingMachine_type, voltage text);