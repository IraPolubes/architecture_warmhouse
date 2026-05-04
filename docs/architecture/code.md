# C4 Code Diagram

Структура кода Go-приложения Smart Home API (уровень классов/структур).

```plantuml
@startuml
!include ../C4_templates/C4.puml

title C4 Code Diagram — Smart Home API

package "main" {
    class main {
        +main()
        -getEnv(key, default) string
    }
}

package "handlers" {
    class SensorHandler {
        +DB : *db.DB
        +TemperatureService : *services.TemperatureService
        +RegisterRoutes(router)
        +GetSensors(c)
        +GetSensorByID(c)
        +CreateSensor(c)
        +UpdateSensor(c)
        +DeleteSensor(c)
        +UpdateSensorValue(c)
        +GetTemperatureByLocation(c)
    }
}

package "services" {
    class TemperatureService {
        +BaseURL : string
        +HTTPClient : *http.Client
        +GetTemperature(location) : *TemperatureResponse
        +GetTemperatureByID(sensorID) : *TemperatureResponse
    }

    class TemperatureResponse {
        +Value : float64
        +Unit : string
        +Timestamp : time.Time
        +Location : string
        +Status : string
        +SensorID : string
        +Description : string
    }
}

package "db" {
    class DB {
        +Pool : *pgxpool.Pool
        +New(connString) : *DB
        +Close()
        +GetSensors(ctx) : []Sensor
        +GetSensorByID(ctx, id) : Sensor
        +CreateSensor(ctx, s) : Sensor
        +UpdateSensor(ctx, id, s) : Sensor
        +DeleteSensor(ctx, id)
    }
}

package "models" {
    class Sensor {
        +ID : int
        +Name : string
        +Type : SensorType
        +Location : string
        +Value : float64
        +Unit : string
        +Status : string
        +LastUpdated : time.Time
        +CreatedAt : time.Time
    }

    class SensorCreate {
        +Name : string
        +Type : SensorType
        +Location : string
        +Unit : string
    }

    class SensorUpdate {
        +Name : string
        +Type : SensorType
        +Location : string
        +Value : *float64
        +Unit : string
        +Status : string
    }
}

main --> SensorHandler : creates
main --> DB : creates
main --> TemperatureService : creates
SensorHandler --> DB : uses
SensorHandler --> TemperatureService : uses
DB --> Sensor : returns
DB --> SensorCreate : accepts
DB --> SensorUpdate : accepts
TemperatureService --> TemperatureResponse : returns

@enduml
```
