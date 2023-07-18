currencies = {'USD':1.0, 'EUR':0.892, 'JPY':138.8, 'GBP':1.309, 'CHF':0.862,
              'CAD':1.322, 'AUD':1.462 }

def convert(usd):
    for cur in currencies:
        print(cur, f"{{gap}}")

convert(124)