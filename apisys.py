import openmeteo_requests
import pgeocode

#cache 
def weatherAPI(zipcode):
    openmeteo = openmeteo_requests.Client()

    # temu shipping with the zip code
    nominatim=pgeocode.Nominatim("US")
    data = nominatim.query_postal_code(zipcode)
    print("apisys zipcode: " + zipcode)
    latitude = data["latitude"]
    longitude = data["longitude"]

    if latitude != latitude or longitude != longitude:
        raise ValueError("Please enter a valid US ZIP code.")

    # api? more like app is boring
    print("Fetching API.")
    url="https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": ["temperature_2m", "precipitation", "wind_speed_10m"],
        "current": ["temperature_2m", "precipitation", "wind_speed_10m"],
        "timezone": "US/Central",
        "wind_speed_unit": "mph",
        "temperature_unit": "fahrenheit",
        "precipitation_unit": "inch"
    }

    # go fetch boy
    responses = openmeteo.weather_api(url, params=params)
    response = responses[0]
    print(response)

    currentweather = response.Current()
    currentTemp = currentweather.Variables(0).Value()
    currentPrecipitation = currentweather.Variables(1).Value()
    currentWind = currentweather.Variables(2).Value()
    
    return currentTemp, currentPrecipitation, currentWind
