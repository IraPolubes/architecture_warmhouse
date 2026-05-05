# C4 Component Diagram - Device Registration and Configuration Service

Какие компоненты составляют контейнер `Device Registration and Configuration Service`.

```plantuml
@startuml
!include ../C4_templates/C4_Component.puml

title C4 Component Diagram - Device Registration and Configuration Service

Container(api, "Smart Home API", "Backend API", "Entry point for frontend requests")
ContainerDb(deviceDb, "Device State and Commands Database", "Relational / Document Database", "Stores devices, device states, commands, and automation scenarios")

Container_Boundary(deviceService, "Device Registration and Configuration Service") {

    Component(deviceController, "Device Registration Controller", "REST Controller", "Receives requests to register and configure devices")

    Component(deviceAppService, "Device Registration Application Service", "Application Service", "Executes device registration and configuration use cases")

    Component(deviceRegistry, "Device Registry", "Domain Component", "Checks device identity, uniqueness, and ownership")

    Component(deviceRepository, "Device Repository", "Repository", "Reads and writes device registration and configuration data")
}

Rel(api, deviceController, "Calls", "HTTP / JSON")
Rel(deviceController, deviceAppService, "Calls use case methods")
Rel(deviceAppService, deviceRegistry, "Checks device identity and ownership")
Rel(deviceAppService, deviceRepository, "Reads and writes device data")
Rel(deviceRepository, deviceDb, "Reads from and writes to", "SQL / NoSQL")

@enduml
```
