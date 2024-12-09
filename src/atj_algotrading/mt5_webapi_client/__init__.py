import requests
import pandas as pd

class MT5_Client:
    def __init__(self, url, request_timeout=10):
        self.url = url
        self.request_timeout = request_timeout

    def initialize(self):
        res = requests.get(f'{self.url}/initialize', timeout=self.request_timeout)

        if res.status_code == 200:
            return res.json()


    def login(self):
        res = requests.get(f'{self.url}/login', timeout=self.request_timeout)

        if res.status_code == 200:
            return res.json()


    def account_info(self):
        res = requests.get(f'{self.url}/account-info', timeout=self.request_timeout)

        if res.status_code == 200:
            return res.json()

    def symbols(self):
        res = requests.get(f'{self.url}/get-symbols', timeout=self.request_timeout)

        if res.status_code == 200:
            df = pd.DataFrame(res.json())
            return df

    def symbol_info(self, symbol):
        res = requests.get(f'{self.url}/get-symbol-info', params={"symbol": symbol}, timeout=self.request_timeout)

        if res.status_code == 200:
            return res.json()

    def symbol_info_tick(self, symbol):
        res = requests.get(f'{self.url}/get-symbol-tick', params={"symbol": symbol}, timeout=self.request_timeout)

        if res.status_code == 200:
            return res.json()
    def num_orders(self):
        res = requests.get(f'{self.url}/get-symbols', timeout=self.request_timeout)

        if res.status_code == 200:
            return res.json()

    def orders(self):
        res = requests.get(f'{self.url}/get-orders', timeout=self.request_timeout)

        if res.status_code == 200:
            df = pd.DataFrame(res.json())
            return df

    def num_positions(self):
        res = requests.get(f'{self.url}/get-num-positions', timeout=self.request_timeout)

        if res.status_code == 200:
            return res.json()

    def positions(self):
        res = requests.get(f'{self.url}/get-positions', timeout=self.request_timeout)

        if res.status_code == 200:
            df = pd.DataFrame(res.json())
            return df

    def history_orders(self, start_dt, end_dt):
        res = requests.get(f'{self.url}/get-history-orders', params={'start-dt': start_dt, 'end-dt': end_dt},
                           timeout=self.request_timeout)
        if res.status_code == 200:
            df = pd.DataFrame(res.json())
            return df

    def history_deals(self, start_dt, end_dt):
        res = requests.get(f'{self.url}/get-history-deals', params={'start-dt': start_dt, 'end-dt': end_dt},
                           timeout=self.request_timeout)
        if res.status_code == 200:
            df = pd.DataFrame(res.json())
            return df

    def get_ohlc(self, symbol, timeframe, start_dt, end_dt):
        res = requests.get(f'{self.url}/ohlc-data',
                           params={'symbol': symbol, 'timeframe': timeframe, 'start-dt': start_dt, 'end-dt': end_dt},
                           timeout=self.request_timeout)

        if res.status_code == 200:
            df = pd.DataFrame(res.json())
            return df

    def get_ticks(self, symbol, start_dt, end_dt):
        res = requests.get(f'{self.url}/get-ticks',
                           params={'symbol': symbol, 'start-dt': start_dt, 'end-dt': end_dt},
                           timeout=self.request_timeout)

        if res.status_code == 200:
            df = pd.DataFrame(res.json())
            return df