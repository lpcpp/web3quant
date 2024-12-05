# -*- coding: utf-8 -*-
"""
    okx API
"""

import json
import datetime
from okx import PublicData  # pylint: disable=E0401
from utils import is_file_exist


class OkxAPI(object):
    """okx api"""

    def __init__(self):
        self.fn = './result/okx_instruments_' + datetime.datetime.now().strftime('%Y-%m-%d') + '.json'

    def write_all_instrument_to_json_file(self):
        """
        desc: 获取所有的现货列表, 写入到json文件
        url: https://www.okx.com/docs-v5/zh/?python#trading-account-rest-api-get-instruments
        """
        flag = "0"  # 实盘:0 , 模拟盘：1
        publicDataAPI = PublicData.PublicAPI(flag=flag)

        # 检查当天是否运行过
        if not is_file_exist(self.fn):
            # 获取交易产品基础信息
            result = publicDataAPI.get_instruments(
                instType="SPOT"
            )
            # 将运行结果写入到文件
            with open(self.fn, 'w', encoding='utf-8') as f:
                f.write(json.dumps(result))

    def get_all_usdt_spot_pair(self):
        """
        desc: 获取所有的usdt计价的现货
        """
        self.write_all_instrument_to_json_file()
        quoteCcy = "USDT"
        count = 0
        data = json.load(open(self.fn, 'r', encoding='utf-8'))
        spot_list = []
        for item in data['data']:
            if item['quoteCcy'] == quoteCcy:
                count += 1
                spot_list.append(item['baseCcy'])
                # print(
                #     # " instId=" + item['instId'] + '\n',
                #     item['baseCcy'],
                #     datetime.datetime.fromtimestamp(int(item['listTime']) / 1000).strftime("%Y-%m-%d"),
                # )
        print('okx交易所中usdt计价的现货总数为', count)
        return spot_list


if __name__ == "__main__":
    pass