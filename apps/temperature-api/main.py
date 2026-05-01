from fastapi import FastAPI, HTTPException
from datetime import datetime, timezone
import random

app = FastAPI()
SENSOR_ID_TO_LOCATION = {
    "1": "Living Room",
    "2": "Bedroom",
    "3": "Kitchen",
}

LOCATION_TO_SENSOR_ID = {
    "Living Room": "1",
    "Bedroom": "2",
    "Kitchen": "3",
}

@app.get("/temperature")
def get_temperature(location: Optional[str] = "", sensorId: Optional[str] = ""):

    if location == "":
        location = SENSOR_ID_TO_LOCATION.get(sensorId, "Unknown")

    if sensorId == "":
        sensorId = LOCATION_TO_SENSOR_ID.get(location, "0")

    if location == "Unknown" and sensorId == "0":
        raise HTTPException(status_code=400, detail="location or sensorId is required")

    return {
        "value": round(random.uniform(-25, 50), 1),
        "unit": "celsius",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "location": location,
        "status": "ok",
        "sensor_id": sensorId,
        "sensor_type": "temperature",
        "description": f"Random temperature for {location}"
    }