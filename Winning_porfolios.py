# First we import the library to push data from the internet

# Path: /Users/mateussfeir/Desktop/
# Shortcut Pathway: python serai.py

import requests

# Create a code to send the informations requested

url = 'https://www.alphavantage.co/query'
params = {
    'function' : 'TOURNAMENT_PORTFOLIO',
    'season' : '2022-04',
    'apikey' : 'TE1E1KD330UYLRHQ'
}
response = requests.get(url, params=params)
data = response.json()
# print(data)
for ranking in data['ranking']:
    rank = ranking['rank']
    portfolio = ranking['portfolio']
    variation = float((ranking['percent_gain']))
    print(f'Rank: {rank}')
    print(f'Portfolio: {portfolio}')
    print('Variation: {:.2f}%'.format(variation))
