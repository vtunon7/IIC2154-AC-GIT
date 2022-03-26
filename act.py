from enum import unique
import re
import json
import pandas as pd

file = open('./farmers-protest-tweets-2021-03-5.json')
lista = []
for i in file:
    data = json.loads(i)
    lista.append(data)
tweets = {}
tweets['tweets'] = lista

def top10_retweeted():
    res = sorted(tweets['tweets'], key = lambda x: x['retweetCount'], reverse = True)[:10]
    count = 1
    print('Top 10 tweets mas retweeted:')
    for i in res:
        print(f"{count}) {i['user']['username']}: {i['content']}")
        count += 1

def top10_user_tweets():
    print('Top 10 usuarios con más tweets')
    count = 1
    count2 = 1
    filtrados = list({i['user']['id']:i for i in tweets['tweets']}.values())
    res3 = sorted(filtrados, key = lambda x: x['user']['statusesCount'], reverse = True)[:10]
    for i in res3:
        print(f"{count2}) {i['user']['username']} {i['user']['statusesCount']}")
        count2 += 1


file.close()
# raw_tweets = pd.read_json(r'./farmers-protest-tweets-2021-03-5.json', lines=True)
# raw_tweets = raw_tweets[raw_tweets['lang']=='en']
# print("Shape: ", raw_twee1ts.shape)
# print(raw_tweets.head(5))
top10_user_tweets()
