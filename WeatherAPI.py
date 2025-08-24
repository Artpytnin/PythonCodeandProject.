import requests

api_key = "29d17e7e263b18886e87b7cc7d2e9fa6"


# https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
def get_current_weather_by_coord(lat, lon , api_key) :
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"

    response = requests.get(url)

    if response.status_code == 200 :
        weather_data = response.json()
    
        temparature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        description = weather_data['weather'][0]['description']

        print(f"Temperature : {temparature} K")
        print(f"Humidity : {humidity} %")
        print(f"Description : {description} ")




    else :
        print("API Error")


    # https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
def get_current_weather_by_city(city_name , api_key) :
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

    response = requests.get(url)

    if response.status_code == 200 :
        weather_data = response.json()
    
        temparature = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        description = weather_data['weather'][0]['description']

        print(f"Temperature : {temparature} K")
        print(f"Humidity : {humidity} %")
        print(f"Description : {description} ")




    else :
        print("API Error")


#get_current_weather_by_coord(13.787976402522686, 100.61006288011345 , api_key)
get_current_weather_by_city("Tokyo" , api_key)
