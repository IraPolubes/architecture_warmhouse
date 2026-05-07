@startuml

title ER Diagram — Smart Home

entity "User" as user {
  * id : UUID
  --
  name : varchar
  email : varchar
}

entity "Home" as home {
  * id : UUID
  --
  user_id : UUID <<FK>>
  name : varchar
  address : varchar
}

entity "Module" as module {
  * id : UUID
  --
  home_id : UUID <<FK>>
  name : varchar
  description : varchar
}

entity "DeviceType" as device_type {
  * id : UUID
  --
  name : varchar
  description : varchar
}

entity "Device" as device {
  * id : UUID
  --
  type_id : UUID <<FK>>
  home_id : UUID <<FK>>
  module_id : UUID <<FK>>
  serial_number : varchar
  status : varchar
}

entity "TelemetryData" as telemetry_data {
  * id : UUID
  --
  device_id : UUID <<FK>>
  temperature : float
  status : varchar
  recorded_at : timestamp
}

user ||--o{ home : owns
home ||--o{ module : contains
home ||--o{ device : contains
module ||--o{ device : groups
device_type ||--o{ device : classifies
device ||--o{ telemetry_data : generates

@enduml