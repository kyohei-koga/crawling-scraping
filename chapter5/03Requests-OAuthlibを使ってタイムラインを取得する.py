import pandas as pd
from requests_oauthlib import OAuth1Session

path = '/home/kyohei/crawling-scraping/chapter5/api.csv'
api = pd.read_csv(path, header=None, names=['name', 'value'])

# 認証情報を取得する。
CONSUMER_KEY = api.loc[0, 'value']
CONSUMER_SECRET = api.loc[1, 'value']
ACCESS_TOKEN = api.loc[2, 'value']
ACCESS_TOKEN_SECRET = api.loc[3, 'value']

# 認証情報を使ってOAuth1Sessionオブジェクトを得る。
twitter = OAuth1Session(CONSUMER_KEY,
                        client_secret=CONSUMER_SECRET,
                        resource_owner_key=ACCESS_TOKEN,
                        resource_owner_secret=ACCESS_TOKEN_SECRET)

# ユーザーのタイムラインを取得する。
response = twitter.get('https://api.twitter.com/1.1/statuses/home_timeline.json')

# APIのレスポンスはJSON形式の文字列なので、response.json()でパースしてlistを取得できる。
# statusはツイート（Twitter APIではStatusと呼ばれる）を表すdict。
for status in response.json():
    print('@' + status['user']['screen_name'], status['text'])  # ユーザー名とツイートを表示する。
