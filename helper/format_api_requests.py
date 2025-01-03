import json
import os


def extract_crypto_info(crypto_data):
    crypto_name = crypto_data['data']['1']['name']
    crypto_symbol = crypto_data['data']['1']['symbol']
    crypto_price = crypto_data['data']['1']['quote']['USD']['price']
    crypto_market_cap = crypto_data['data']['1']['quote']['USD']['market_cap']

    formatted_price = "{:.2f}".format(crypto_price)
    formatted_market_cap = "{:.2f}".format(crypto_market_cap)

    return (
        crypto_name,
        crypto_symbol,
        formatted_price,
        formatted_market_cap
    )


def get_city_id(city):
    json_file_path = os.path.join(os.path.dirname(__file__), 'city_list.json')
    with open(json_file_path) as json_file:
        data = json.load(json_file)
        for item in data:
            if item['name'] == city:
                return item['id']
    return None


def extract_weather_info(weather_data):
    weather_info = {}

    weather_info['weather'] = weather_data['weather'][0]['main']
    temp = str(weather_data['main']['temp'])
    weather_info['temp'] = temp[:2] + '.' + temp[2:3]
    weather_info['wind_speed'] = weather_data['wind']['speed']

    return weather_info

