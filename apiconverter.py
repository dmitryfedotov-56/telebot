import json
import requests


class APIConverter():

    @staticmethod
    def convert_values(amount: float, from_code: str, into_code: str):
        request = f'https://min-api.cryptocompare.com/data/price?fsym={from_code}&tsyms={into_code}'
        r = requests.get(request)
        return float(json.loads(r.content)[into_code]) * amount

