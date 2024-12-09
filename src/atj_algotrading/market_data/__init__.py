import requests
import pandas as pd

class MarketData:
    def __init__(self, source_url='https://tradinglabs.atj-traders.com/api', api_key='free'):
        self.url = source_url

    def symbols(self):
        res = requests.get(f'{self.url}/get-symbols')

        if res.status_code == 200:
            df = pd.DataFrame(res.json())
            return df

    def symbol_info(self, symbol):
        res = requests.get(f'{self.url}/get-symbol-info', params={"symbol": symbol})

        if res.status_code == 200:
            return res.json()

    def get_ohlc(self, symbol, timeframe, start_dt, end_dt):
        res = requests.get(f'{self.url}/ohlc-data',
                           params={'symbol': symbol, 'timeframe': timeframe, 'start-dt': start_dt, 'end-dt': end_dt})

        if res.status_code == 200:
            df = pd.DataFrame(res.json())
            return df