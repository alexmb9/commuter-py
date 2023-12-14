import asyncio
import config

from traveltimepy import ProtoCountry, Coordinates, ProtoTransportation, TravelTimeSdk

async def main():
    sdk = TravelTimeSdk(config.app_id, config.api_key)

    travel_times = await sdk.time_filter_proto_async(
        origin=Coordinates(lat=51.508930, lng=-0.131387),
        destinations=[
            Coordinates(lat=51.508824, lng=-0.167093)
        ],
        transportation=ProtoTransportation.DRIVING_FERRY,
        travel_time=7200,
        country=ProtoCountry.UNITED_KINGDOM
    )
    
    print(travel_times)

asyncio.run(main())