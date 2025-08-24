import requests

def get_country_info(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"


    response = requests.get(url)


    if response.status_code == 200 :
        country_data = response.json()[0]


        name = country_data ["name"]["official"]
        capital = country_data['capital'][0]
        population = country_data['population']


        print(f"country:{name}")
        print(f"capital: {capital}")
        print(f"population: {population}")

        
    else:
        print("country not found or API Error. |", response.status_code)

get_country_info("Japan")
