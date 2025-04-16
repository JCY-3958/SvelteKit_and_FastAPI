import asyncio
import json

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sse_starlette.sse import EventSourceResponse

from .sensor import SensorData

app = FastAPI()
sensor = SensorData()

app.add_middleware(
	CORSMiddleware,
	allow_origins=["http://localhost:5173"],
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to the Sensor Dashboard API"}

@app.get("/current")
async def get_current_reading():
    #Get the current Sensor reading
    return sensor.generate_reading()

@app.get("/stream")
async def stream_data():
    #Stream sensor data using server-sent events
    async def event_generator():
        while True:
            data = sensor.generate_reading()
            yield {
				"event": "sensor_update",
				"data": json.dumps(data)
			}
            await asyncio.sleep(1) #updata every 1 seconds
            
    return EventSourceResponse(event_generator())