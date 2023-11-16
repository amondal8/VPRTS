import requests

params = {
      'access_key': 'a59812d5080671276d92a63d43fc4a2a',
      'limit': '10',
      'flight_status':'active'
}

api_result = requests.get('http://api.aviationstack.com/v1/flights', params)

api_response = api_result.json()

print(api_response)

for flight in api_response['data']:
    if flight['flight_status']:
    # print("I am here")
        print('{} flight {} from {} ({}) to {} ({}) is in the air.\n'.format(
            flight['airline']['name'],
            flight['flight']['iata'],
            flight['departure']['airport'],
            flight['departure']['iata'],
            flight['arrival']['airport'],
            flight['arrival']['iata']))
    # else:
    #     print("All flights landed")