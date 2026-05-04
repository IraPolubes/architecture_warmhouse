# C4 Component Diagram

Компоненты внутри Go-приложения Smart Home API.

```plantuml
@startuml
!include ../C4_templates/C4_Component.puml

title C4 Component Diagram — Smart Home API

Container_Boundary(goApp, "Smart Home API (Go)") {
    Component(handlers, "Handlers", "Go, Gin", "HTTP request handlers for sensors CRUD")
    Component(services, "TemperatureService", "Go", "Fetches real-time temperature from external API")
    Component(dbPkg, "DB Package", "Go, pgx", "Database access layer")
    Component(models, "Models", "Go", "Domain models: Sensor, SensorCreate, SensorUpdate")
}

ContainerDb(db, "PostgreSQL", "PostgreSQL", "Stores sensors data")
Container(tempApi, "Temperature API", "Python", "External temperature service")

Rel(handlers, dbPkg, "CRUD operations")
Rel(handlers, services, "GetTemperature()")
Rel(handlers, models, "Uses types")
Rel(dbPkg, models, "Maps rows to structs")
Rel(dbPkg, db, "SQL queries", "pgxpool")
Rel(services, tempApi, "HTTP GET", "/temperature")

@enduml
```
