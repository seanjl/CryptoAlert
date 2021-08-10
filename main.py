import requests
import emailAlert
import keys
import pandas as pd
from time import sleep

# Sean Leitch, 10th August 2021
# In this example I'm using ETH and EUR, but you can choose the currency you want

def get_crypto_rates(base_currency='EUR', assets='ETH'):
    url = 'https://api.nomics.com/v1/currencies/ticker'

    payload = {'key': keys.NOMICS_API_KEY, 'convert': base_currency, 'ids': assets, 'interval': '1d'}
    response = requests.get(url, params=payload)
    data = response.json()

    crypto_currency, crypto_price, crypto_timestamp = [], [], []

    for asset in data:
        crypto_currency.append((asset['currency']))
        crypto_price.append((asset['price']))
        crypto_timestamp.append((asset['price_timestamp']))

    raw_data = {
        'assets': crypto_currency,
        'rates': crypto_price,
        'timestamp': crypto_timestamp
    }

    df = pd.DataFrame(raw_data)
    print(df)
    return df

# Advises the user on what choice to make
def set_alert(dataframe, asset, alert_high_price, alert_low_price):
    crypto_value = float(dataframe[dataframe['assets'] == asset]['rates'].item())

    details = f'{asset}: {crypto_value}, HighPriceAlert: {alert_high_price}, LowPriceAlert: {alert_low_price}'

    if crypto_value >= alert_high_price:
        print((details + ' << COIN IS EXPENSIVE! SELL NOW!'))
        emailAlert.sendEmailAlertSell()
    else:
        if crypto_value <= alert_low_price:
            print((details + ' << COIN IS CHEAP! BUY NOW!'))
            emailAlert.sendEmailAlertBuy()
        else:
            print((details + ' << KEEP HOLDING!'))

# Refresh alert every 30s
loop = 0
while True:
    print(f'----------------------({loop})----------------------')

    try:
        df = get_crypto_rates()
        set_alert(df, 'ETH', 2750, 1600) # Here is where you choose highPriceAlert and lowPriceAlert
    except Exception as e:
        print('API Request failed...trying again')

    loop += 1
    sleep(30)