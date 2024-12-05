# -*- coding: utf-8 -*-
"""
    CoinMarket API
"""
import datetime
import requests

from utils import is_file_exist
from settings import COINMARKET_SETTING


class CoinMarketAPI:
    """
    CoinMarket API
    """
    def __init__(self):
        self.headers = {
            'Accepts': 'application/json',
            'Accept-Encoding': 'deflate, gzip',
            'X-CMC_PRO_API_KEY': COINMARKET_SETTING['apikey'],
        }

        self.list_fn = './result/coinmarket_list_' + datetime.datetime.now().strftime('%Y-%m-%d') + '.json'
        self.info_fn = './result/coinmarket_info_' + datetime.datetime.now().strftime('%Y-%m-%d') + '.json'
        self.map_fn = './result/coinmarket_map_' + datetime.datetime.now().strftime('%Y-%m-%d') + '.json'

    def write_currency_list_to_json_file(self):
        """
        desc: 获取所有的coinmarket市场的前5000市值的币种
        url: https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyListingsLatest
        """
        parameters = {
            'start':'1',
            'limit':'5000',
            'convert':'USD'
        }
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        if not is_file_exist(self.list_fn):
            res = requests.get(url, params=parameters, headers=self.headers, timeout=60)
            with open (self.list_fn, 'w', encoding='utf-8') as f:
                f.write(res.text)

    def get_currency_map(self):
        """
        desc: Returns a mapping of all cryptocurrencies to unique CoinMarketCap ids
        url: https://coinmarketcap.com/api/documentation/v1/#operation/getV1CryptocurrencyMap
        """
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/map'
        if not is_file_exist(self.map_fn):
            res = requests.get(url, headers=self.headers,timeout=60)
            with open (self.map_fn, 'w', encoding='utf-8') as f:
                f.write(res.text)

    def get_currency_info(self):
        """
        desc:Returns all static metadata available for one or more cryptocurrencies
        url: https://coinmarketcap.com/api/documentation/v1/#operation/getV2CryptocurrencyInfo
        """
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/info?id=1'
        if not is_file_exist(self.info_fn):
            res = requests.get(url, headers=self.headers, timeout=60)
            with open (self.info_fn, 'w', encoding='utf-8') as f:
                f.write(res.text)


if __name__ == '__main__':
    pass