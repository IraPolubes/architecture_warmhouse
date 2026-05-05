# C4 Component Diagram - User Management Service

Какие компоненты составляют контейнер `User Management Service`.

```plantuml
@startuml
!include ../C4_templates/C4_Component.puml

title C4 Component Diagram - User Management Service

Container(api, "Smart Home API", "Backend API", "Entry point for frontend requests")
ContainerDb(userDb, "User Database", "Relational Database", "Stores users, credentials, addresses, homes, and roles")

Container_Boundary(authService, "User Management Service") {

    Component(userController, "User Account Controller", "REST Controller", "Receives authentication and registration requests")

    Component(userAppService, "User Account Application Service", "Application Service", "Executes user account use cases")

    Component(tokenService, "Token Service", "Domain / Security Component", "Issues and validates authentication tokens")

    Component(userRepository, "User Repository", "Repository", "Reads and writes user account data")
}

Rel(api, userController, "Calls", "HTTP / JSON")
Rel(userController, userAppService, "Calls use case methods")
Rel(userAppService, tokenService, "Uses")
Rel(userAppService, userRepository, "Reads and writes user data")
Rel(userRepository, userDb, "Reads from and writes to", "SQL")

@enduml
```
