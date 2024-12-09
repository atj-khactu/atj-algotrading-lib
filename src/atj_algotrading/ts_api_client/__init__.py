import os
import requests
from datetime import datetime, timedelta
from time import sleep
import pandas as pd

class TsClient:
    def __init__(self):
        self.client_id = os.environ['ts_client_id']
        self.client_secret = os.environ['ts_client_secret']
        self.refresh_token = os.environ['ts_refresh_token']
        self.access_token = ''
        self.access_token_expiry = datetime.now()

    def refresh_access_token(self):
        url = 'https://signin.tradestation.com/oauth/token'

        data = {
            'grant_type': 'refresh_token',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'refresh_token': self.refresh_token,
        }

        res = requests.post(url, headers={'Content-Type': 'application/x-www-form-urlencoded'}, data=data)

        token_data = res.json()

        self.access_token = token_data['access_token']
        self.access_token_expiry = datetime.now() + timedelta(seconds = token_data['expires_in'])


    def check_access_token(self):
        if self.access_token_expiry < datetime.now() + timedelta(minutes=2):
            self.refresh_access_token()


    def get_bars(self, symbol):
        self.check_access_token()

        url = f'https://api.tradestation.com/v3/marketdata/barcharts/{symbol}'

        headers = {'Authorization': f'Bearer {self.access_token}'}

        params = {
            'interval': '15',
            'unit': 'Minute',
            'firstdate': "2024-12-09T00:00:00Z",
            'lastdate': "2024-12-09T18:00:00Z",
        }

        response = requests.request("GET", url, headers=headers, params=params)
        df = pd.DataFrame(response.json()['Bars'])
        print(df.columns)

        return df



if __name__ == '__main__':
    ts_client = TsClient()

    df = ts_client.get_bars('CLF25')
    print(df)

