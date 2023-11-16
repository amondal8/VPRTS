import requests

# Set the API endpoint and parameters
api_endpoint = "https://flightera-flight-data.p.rapidapi.com/aircraft/search"
headers = {
    "X-RapidAPI-Key": "33a8580aedmsh8671a7ccc17edb6p199a69jsn60133bbc4c3c",
    "X-RapidAPI-Host": "flightera-flight-data.p.rapidapi.com"
}
params = {
    "originPlace": "CODE_FROM",
    "destinationPlace": "CODE_TO",
    "outboundDate": "2023-05-06",
    "inboundDate": "2023-05-08",
    "currency": "USD"
}

# Send the API request and parse the response
response = requests.get(api_endpoint, headers=headers, params=params)
json_data = response.json()

print(json_data)

# Extract the flight details from the response
# quotes = json_data["Quotes"]
# carriers = json_data["Carriers"]
# places = json_data["Places"]
#
# # Print the flight details
# print("Quotes:")
# for quote in quotes:
#     outbound_carrier = next((c for c in carriers if c["CarrierId"] == quote["OutboundLeg"]["CarrierIds"][0]), None)
#     inbound_carrier = next((c for c in carriers if c["CarrierId"] == quote["InboundLeg"]["CarrierIds"][0]), None)
#     outbound_origin = next((p for p in places if p["PlaceId"] == quote["OutboundLeg"]["OriginId"]), None)
#     outbound_destination = next((p for p in places if p["PlaceId"] == quote["OutboundLeg"]["DestinationId"]), None)
#     inbound_origin = next((p for p in places if p["PlaceId"] == quote["InboundLeg"]["OriginId"]), None)
#     inbound_destination = next((p for p in places if p["PlaceId"] == quote["InboundLeg"]["DestinationId"]), None)
#     print(f"{outbound_carrier['Name']} from {outbound_origin['Name']} to {outbound_destination['Name']}: {quote['MinPrice']} {params['currency']}")
#     print(f"{inbound_carrier['Name']} from {inbound_origin['Name']} to {inbound_destination['Name']}: {quote['InboundLeg']['MinPrice']} {params['currency']}")
