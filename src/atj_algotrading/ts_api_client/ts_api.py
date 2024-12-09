import os
import requests
import urllib.parse

if __name__ == '__main__':
    url = 'https://signin.tradestation.com/authorize'

    params = {
        'response_type': 'code',
        'client_id': os.environ['ts_client_id'],
        'audience': 'https://api.tradestation.com',
        'redirect_uri': 'http://localhost:3000',
        'state': '1',
        'scope': ' '.join(['openid', 'offline_access', 'MarketData']),
    }

    print(url + '?' + urllib.parse.urlencode(params))