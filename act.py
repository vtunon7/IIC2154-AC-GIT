from enum import unique
import re
import json
import pandas as pd
from collections import Counter

file = open('./farmers-protest-tweets-2021-03-5.json')
lista = []
for i in file:
    data = json.loads(i)
    lista.append(data)
tweets = {}
tweets['tweets'] = lista

file.close()

def top10_retweeted():
    res = sorted(tweets['tweets'], key = lambda x: x['retweetCount'], reverse = True)[:10]
    count = 1
    print('Top 10 tweets mas retweeted:')
    for i in res:
        print(f"{count}) {i['user']['username']}: {i['content']}")
        count += 1

def top10_user_tweets():
    print('Top 10 usuarios con más tweets')
    count2 = 1
    filtrados = list({i['user']['id']:i for i in tweets['tweets']}.values())
    res3 = sorted(filtrados, key = lambda x: x['user']['statusesCount'], reverse = True)[:10]
    for i in res3:
        print(f"{count2}) {i['user']['username']} {i['user']['statusesCount']}")
        count2 += 1

def top10_days_tweets():
    lista_dias = []
    for i in tweets['tweets']:
        dia = i['date'][:10]
        lista_dias.append(dia)
    dias = Counter(lista_dias)
    cont = 1
    for i, j in dias.most_common(10):
        print(f"{cont}) {i}: {j}")
        cont += 1


def top10_hashtags():
    lista_hash = []
    for i in tweets['tweets']:
        tweet = i['content']
        x = re.findall(r"#(\w+)", tweet)
        lista_hash.append(x)

    lista_hash2 = []
    for i in lista_hash:
        for j in i:
            lista_hash2.append(j)

    cont = 1
    hashtags = Counter(lista_hash2)
    for i, j in hashtags.most_common(10):
        print(f"{cont}) #{i}: {j}")
        cont += 1
