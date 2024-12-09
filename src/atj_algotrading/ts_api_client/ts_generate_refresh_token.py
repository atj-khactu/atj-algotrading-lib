import requests
import os

auth_code = '7wErOA8FcsFj9lv4jXcAyeke4lLJPfYZ0BlkGD9mDtu0g'


if __name__ == '__main__':

    url = 'https://signin.tradestation.com/oauth/token'

    data = {
        'grant_type': 'authorization_code',
        'client_id': os.environ['ts_client_id'],
        'client_secret': os.environ['ts_client_secret'],
        'code': auth_code,
        'redirect_uri': 'http://localhost:3000'
    }

    res = requests.post(url, headers={'Content-Type': 'application/x-www-form-urlencoded'}, data=data)
    print(res.text)

    token_data = res.json()
