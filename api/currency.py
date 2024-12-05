import json
import os
from api.api_coinmarket import CoinMarketAPI
from api.api_okx import OkxAPI

from utils import is_file_exist


class Currency():
    """
    现货数据入口
    """

    def __init__(self):
        self.okx_api = OkxAPI()
        self.coinmarket_api = CoinMarketAPI()
        self.spot_usdt_list = None
        self.spot_coinmarket_list = None
        self.currency_json_fn = os.path.join(os.path.abspath('.'), 'result', 'currency.csv')

    def get_currency_with_marketcap(self, start=0, end=10**100, output="console"):
        """
        根据marketcap筛选加密货币标的, 将结果输出到终端窗口或者csv文件中
        """
        self.spot_usdt_list = self.okx_api.get_all_usdt_spot_pair()
        self.coinmarket_api.write_currency_list_to_json_file()

        count = 0
        coinmarket_data = json.load(open(self.coinmarket_api.list_fn, 'r', encoding='utf-8'))
        if output == 'console':
            from prettytable import PrettyTable  # pylint: disable=C0415,E0401
            table = PrettyTable()
            table.field_names = ["ID", "synbol", "max_supply", "circulating_supply", "market_cap", "fully_diluted_market_cap", "price"]
        else:
            import csv  # pylint: disable=C0415
            # if is_file_exist(self.currency_json_fn):
            #     fd = open(self.currency_json_fn, 'w', encoding='utf-8')
            # else:
            fd = open(self.currency_json_fn, 'w', encoding='utf-8')

            writer = csv.writer(fd)
            writer.writerow(
                ["ID", "synbol", "max_supply", "circulating_supply", "market_cap", "fully_diluted_market_cap", "price"]
            )

        for item in coinmarket_data['data']:
            if start < item['quote']['USD']['market_cap'] < end and item["symbol"] in self.spot_usdt_list:
                count += 1
                if output == "console":
                    table.add_row([item["id"],
                                item["symbol"],
                                item["max_supply"],
                                item["circulating_supply"],
                                item["quote"]['USD']['market_cap'],
                                item["quote"]['USD']['fully_diluted_market_cap'],
                                item["quote"]['USD']['price']
                                ])
                elif output == "csv":
                    writer.writerow([item["id"],
                            item["symbol"],
                            item["max_supply"],
                            item["circulating_supply"],
                            item["quote"]['USD']['market_cap'],
                            item["quote"]['USD']['fully_diluted_market_cap'],
                            item["quote"]['USD']['price']
                            ])
        if output == 'console':
            print(table)
        elif output == 'csv':
            fd.close()

        print('筛选出的标的总数为：', count)