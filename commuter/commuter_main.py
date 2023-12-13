import asyncio
from datetime import datetime

from traveltimepy import Location, Coordinates, PublicTransport, Property, FullRange, TravelTimeSdk

from traveltimepy import Driving, Coordinates, TravelTimeSdk

async def main():
    sdk = TravelTimeSdk(app_id=config.app_id, api_key=config.api_key)
    
    locations = [
        Location(id="London center", coords=Coordinates(lat=51.508930, lng=-0.131387)),
        Location(id="Hyde Park", coords=Coordinates(lat=51.508824, lng=-0.167093)),
        Location(id="ZSL London Zoo", coords=Coordinates(lat=51.536067, lng=-0.153596))
    ]

    results = await sdk.time_filter_async(
        locations=locations,
        search_ids={
            "London center": ["Hyde Park", "ZSL London Zoo"],
            "ZSL London Zoo": ["Hyde Park", "London center"],
        },
        departure_time=datetime.now(),
        travel_time=3600,
        transportation=PublicTransport(type="bus"),
        properties=[Property.TRAVEL_TIME],
        range=FullRange(enabled=True, max_results=3, width=600)
    )

    print(results)

asyncio.run(main())