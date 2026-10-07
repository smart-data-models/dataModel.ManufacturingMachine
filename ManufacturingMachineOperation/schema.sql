/* (Beta) Export of data model ManufacturingMachineOperation of the subject dataModel.ManufacturingMachine for a PostgreSQL database. Pending translation of enumerations and multityped attributes */
CREATE TYPE ManufacturingMachineOperation_result_type AS ENUM ('aborted', 'failed', 'ok', 'success', 'suspended');
CREATE TYPE ManufacturingMachineOperation_status_type AS ENUM ('cancelled', 'finished', 'ongoing', 'planned', 'scheduled');
CREATE TYPE ManufacturingMachineOperation_type AS ENUM ('ManufacturingMachineOperation');
CREATE TABLE ManufacturingMachineOperation (
  "address" JSON,
  "alternateName" TEXT,
  "areaServed" TEXT,
  "commandSequence" JSON,
  "dataProvider" TEXT,
  "dateCreated" TIMESTAMP,
  "dateModified" TIMESTAMP,
  "description" TEXT,
  "endedAt" TIMESTAMP,
  "id" TEXT PRIMARY KEY,
  "location" JSON,
  "machine" JSON,
  "name" TEXT,
  "operationOutput" JSON,
  "operationType" JSON,
  "operator" JSON,
  "owner" JSON,
  "plannedEndAt" TIMESTAMP,
  "plannedStartAt" TIMESTAMP,
  "result" ManufacturingMachineOperation_result_type,
  "seeAlso" JSON,
  "source" TEXT,
  "startedAt" TIMESTAMP,
  "status" ManufacturingMachineOperation_status_type,
  "type" ManufacturingMachineOperation_type
);