import config
import asyncio
import json
from datetime import datetime

from traveltimepy import Driving, Coordinates, TravelTimeSdk

async def main():
    sdk = TravelTimeSdk(app_id=config.app_id, api_key=config.api_key)
    
    coordinates = [
        Coordinates(lat=51.507609, lng=-0.128315),
        Coordinates(lat=51.517609, lng=-0.138315)
    ]

    # Convert the dictionary to a JSON string
    arrival_time = datetime.now().isoformat()
    data = {
        'coordinates': coordinates,
        'arrival_time': arrival_time,
        'transportation': Driving().dict()
    }
    json_data = json.dumps(data)

    # Pass the JSON string to the method
    results = await sdk.time_map_async(json_data)
    print(results)

asyncio.run(main())