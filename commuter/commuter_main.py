import requests
import json
import config
from datetime import datetime

url = "https://api.traveltimeapp.com/v4/time-filter/fast"

payload = json.dumps({
    "locations": [
    {
      "id": "London center",
      "coords": {
        "lat": 51.508930,
        "lng": -0.131387
      }
    }
  ],
  "arrival_searches": {
    "many_to_one": [
      {
        "id": "arrive-at many-to-one search example",
        "departure_location_ids": [
          "Hyde Park",
          "ZSL London Zoo"
        ],
        "arrival_location_id": "London center",
        "travel_time": 1900,
        "arrival_time_period": "weekday_morning",
        "properties": [
          "travel_time",
        ],
        "transportation": {
          "type": "public_transport"
        }
      }
    ],
    }
})

##could be Accept type needs to be application/geo+json to make the geo json stuff work
headers = {
    'Host': 'api.traveltimeapp.com',
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'X-Application-Id': config.app_id,
    'X-Api-Key': config.app_id
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response)