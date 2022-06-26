import requests


cache = {}

# Get currency you have
currency_code = input()

# Retrieve data for current currency
data = requests.get(f'http://www.floatrates.com/daily/{currency_code}.json').json()

# Add to USD and EUR rates to cache
if 'usd' in data:
    cache['USD'] = data['usd']['rate']
if 'eur' in data:
    cache['EUR'] = data['eur']['rate']

# Get exchange currency and current money amount
while exchange_currency := input():
    money = float(input())

    # Check cache else get from API
    print('Checking the cache...')
    if exchange_currency.upper() in cache:
        print('Oh! It is in the cache!')
    else:
        print('Sorry, but it is not in the cache!')
        cache[exchange_currency.upper()] = data[exchange_currency.lower()]['rate']

    print(f'You received {cache[exchange_currency.upper()] * money} {exchange_currency.upper()}.')