# C4 Container Diagram

Какие контейнеры (приложения, базы данных, сервисы) составляют систему.

```plantuml
@startuml
!include ../C4_templates/C4_Container.puml

title C4 Container Diagram — Smart Home

Person(user, "User", "Manages sensors through a web interface")

System_Boundary(smartHome, "Smart Home System") {
    Container(goApp, "Smart Home API", "Go, Gin", "Handles REST API requests, business logic")
    Container(tempApi, "Temperature API", "Python, Flask", "Returns temperature readings")
    ContainerDb(db, "PostgreSQL", "PostgreSQL", "Stores sensors, users data")
}

System_Ext(sensor, "IoT Sensor", "External temperature sensor")

Rel(user, goApp, "REST API calls", "HTTP/JSON")
Rel(goApp, db, "Reads/Writes sensors", "SQL/pgx")
Rel(goApp, tempApi, "Fetches temperature", "HTTP GET /temperature")
Rel(sensor, tempApi, "Sends readings", "HTTP")

@enduml
```
