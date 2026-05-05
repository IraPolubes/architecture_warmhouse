# C4 Container Diagram

Какие контейнеры (приложения, базы данных, сервисы) составляют систему.

```plantuml
@startuml
!include ../C4_templates/C4_Container.puml

title C4 Container Diagram — Smart Home

title C4 Container Diagram - Smart Home System

Person(user, "User")

System_Boundary(smarthome, "Smart Home System") {

    Container(webApp, "Web Application Frontend",  "React / TypeScript","Provides a web interface for controlling, monitoring configuring devices")

    Container(api, "Smart Home API", "Backend API", "Entry point for the web application. Routes requests to backend services")

    Container(authService, "User Management Service", "Backend Service", "Manages users authentication and registration data")

    Container(controlService, "Device Control Service", "Backend Service", "Controls heating, lighting, and gates")

    Container(deviceService, "Device registration and configuration", "Backend Service", "Registers new devices")

    Container(monitoringService, "Device Monitoring Service", "Backend Service", "Provides telemetry for all devices")

    ContainerDb(userDb, "User Database", "Relational Database", "Stores users, credentials, addresses, homes, and roles")

    ContainerDb(deviceDb, "Device State and Commands Database", "Relational / Document Database", "Stores devices, device states, commands, and automation scenarios")

    ContainerDb(telemetryDb, "Telemetry Database", "Time-Series Database", "Stores telemetry, measurements, and monitoring events")
}



Rel(user, webApp, "Uses", "HTTPS")
Rel(webApp, api, "Sends requests to", "HTTPS / JSON")

Rel(api, authService, "Uses")
Rel(api, controlService, "Uses")
Rel(api, deviceService, "Uses")
Rel(api, monitoringService, "Uses")


Rel(authService, userDb, "Reads from and writes to", "SQL")
Rel(controlService, deviceDb, "Reads from and writes to", "SQL / NoSQL")
Rel(deviceService, deviceDb, "Reads from and writes to", "SQL / NoSQL")
Rel(monitoringService, telemetryDb, "Reads from and writes to", "Time-series queries")


@enduml
```
