# C4 Component Diagram - Web Application Frontend

Какие компоненты составляют контейнер `Web Application Frontend`.

```plantuml
@startuml
!include ../C4_templates/C4_Component.puml

title C4 Component Diagram - Web Application Frontend

Container(api, "Smart Home API", "Backend API", "Entry point for frontend requests")

Container_Boundary(webApp, "Web Application Frontend") {

    Component(pages, "Pages", "React Components", "Screens for authentication, device control, device configuration, and monitoring")

    Component(stateStore, "State Store", "TypeScript State Store", "Stores user session, selected home, devices, and UI state")

    Component(apiClient, "Smart Home API Client", "TypeScript HTTP Client", "Sends requests to the Smart Home API")
}

Rel(pages, stateStore, "Reads from and writes to")
Rel(pages, apiClient, "Uses")
Rel(apiClient, api, "Calls", "HTTPS / JSON")

@enduml
```
