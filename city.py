import argparse
import sys
import requests as requests
import pycountry

parser = argparse.ArgumentParser(description='Get city info')
parser.add_argument(
    'city',
    type=str,
    help='City name'
)

if len(sys.argv) > 2:
    print('System Error')
    sys.exit()

args = parser.parse_args()


class CityDOM:
    def __init__(self, city, country, population, currency):
        self.city = city
        self.country = country
        self.population = population
        self.currency = currency

    def __str__(self):
        return f" ------------" \
               f"\n {self.city} \n " \
               f"\n {self.country} " \
               f"\n {self.currency} " \
               f"\n {self.population} " \
               f"\n ============"


class City:
    API_KEY = 'BcAb5qVG9iQJoEviA2+uWQ==tTFKoLjjsbP5b3D7'
    URL = 'https://api.api-ninjas.com/v1/'

    def __init__(self, city):
        self.city = city.strip().capitalize()

    def get_city_info(self):
        url_city = '{}city?name={}'.format(self.URL, self.city)
        response = requests.get(url_city, headers={'X-Api-Key': f'{self.API_KEY}'})
        if response.status_code == requests.codes.ok:
            response_json = response.json()
            return response_json
        else:
            print("System Error")
            exit()

    def get_country_name_by_code(self, country_code):
        return pycountry.countries.get(alpha_2=country_code)

    def get_country_info(self, country_name):
        url_country = '{}country?name={}'.format(self.URL, country_name)
        response = requests.get(url_country, headers={'X-Api-Key': f'{self.API_KEY}'})
        if response.status_code == requests.codes.ok:
            return response.json()[0]['currency']['code']
        else:
            print("System Error")
            exit()

    def get_info(self):
        city_info = self.get_city_info()
        if len(city_info) >= 1:
            for city in city_info:
                country_name = self.get_country_name_by_code(city["country"]).name
                currency = self.get_country_info(country_name)
                print(CityDOM(self.city, country_name, city['population'], currency))
        else:
            print(f"Invalid city name: {self.city}")


if __name__ == '__main__':
    cityInf = City(args.city)
    cityInf.get_info()
