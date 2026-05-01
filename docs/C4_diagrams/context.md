# Context Diagram
```plantuml
@startuml
!include https://raw.githubusercontent.com/plantuml-stdlib/C4-PlantUML/master/C4_Context.puml

Person(user, "User")
System(system, "Warmhouse")
System_Ext(payment, "sensor")

Rel(user, system, "Uses")
Rel(system, payment, "Gets data from")
@enduml