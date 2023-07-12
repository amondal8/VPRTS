import requests

url = "https://flightera-flight-data.p.rapidapi.com/flight/search"

querystring = {"originPlace": "CODE_FROM",
    "destinationPlace": "CODE_TO",
    "outboundDate": "2023-05-06",
    "inboundDate": "2023-05-08",
    "currency": "USD"}

headers = {
	"X-RapidAPI-Key": "33a8580aedmsh8671a7ccc17edb6p199a69jsn60133bbc4c3c",
	"X-RapidAPI-Host": "flightera-flight-data.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())