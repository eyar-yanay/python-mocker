# payload = {'access_key': '04389f49378e091e9486a3a205dfeacf'}
from request_struct import RatesRequestClass
import json
import requests
from mocker import Mock
from data_example import data

mocker = Mock()

@mocker.mock(RatesRequestClass)
def my_get():
    req = requests.get('http://api.exchangeratesapi.io/v1/latest?access_key=04389f49378e091e9486a3a205dfeacf')
    data = req.json()
    print("I am calling the real api: ", data)
    return data

def get_rates_lower_then_10(data):
    return {k: v for k, v in data['rates'].items() if v < 10}


def main():
    res = my_get()
    print('entire data: ', res)
    rates_lower_then_10 = get_rates_lower_then_10(res)
    print('rates lower then 10', rates_lower_then_10)

main()