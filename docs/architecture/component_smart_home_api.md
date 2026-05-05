# C4 Component Diagram - Smart Home API

Какие компоненты составляют контейнер `Smart Home API`.

```plantuml
@startuml
!include ../C4_templates/C4_Component.puml

title C4 Component Diagram - Smart Home API

Container(webApp, "Web Application Frontend", "React / TypeScript", "Web user interface")
Container(authService, "User Management Service", "Backend Service", "Manages users authentication and registration data")
Container(controlService, "Device Control Service", "Backend Service", "Controls heating, lighting, and gates")
Container(deviceService, "Device Registration and Configuration Service", "Backend Service", "Registers and configures devices")
Container(monitoringService, "Device Monitoring Service", "Backend Service", "Provides telemetry for all devices")

Container_Boundary(api, "Smart Home API") {

    Component(apiRouter, "API Router", "Backend Component", "Routes incoming frontend requests")

    Component(authMiddleware, "Authentication Middleware", "Backend Component", "Checks authentication token and extracts user identity")

    Component(requestValidator, "Request Validator", "Backend Component", "Validates incoming request payloads")

    Component(serviceClients, "Backend Service Clients", "HTTP / gRPC Clients", "Calls internal backend services")

    Component(responseMapper, "Response Mapper", "Backend Component", "Maps backend service responses to frontend response models")
}

Rel(webApp, apiRouter, "Sends requests", "HTTPS / JSON")
Rel(apiRouter, authMiddleware, "Uses")
Rel(authMiddleware, requestValidator, "Forwards authenticated requests")
Rel(requestValidator, serviceClients, "Uses")
Rel(serviceClients, responseMapper, "Returns service responses")

Rel(serviceClients, authService, "Calls")
Rel(serviceClients, controlService, "Calls")
Rel(serviceClients, deviceService, "Calls")
Rel(serviceClients, monitoringService, "Calls")

@enduml
```
