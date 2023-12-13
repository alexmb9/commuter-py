import config
import asyncio
from datetime import datetime
import json

from traveltimepy import Driving, Coordinates, TravelTimeSdk

class CoordinatesEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Coordinates):
            return obj.model_dump()
        return super().default(obj)

async def main():
    sdk = TravelTimeSdk(app_id=config.app_id, api_key=config.api_key)
    
    coordinates = [
        Coordinates(lat=51.507609, lng=-0.128315),
        Coordinates(lat=51.517609, lng=-0.138315)
    ]

    arrival_time = datetime.now().isoformat()
    transportation = Driving().model_dump()

    data = {
        'coordinates': coordinates,
        'arrival_time': arrival_time,
    }

    # Use the custom encoder for serialization
    json_data = json.dumps(data, cls=CoordinatesEncoder)

    # Pass the transportation as a separate argument
    results = await sdk.time_map_async(json_data, transportation)
    print(results)

asyncio.run(main())