currencies = {'USD':1.0, 'EUR':0.892, 'JPY':138.8, 'GBP':1.309, 'CHF':0.862,
              'CAD':1.322, 'AUD':1.462 }

def convert(usd):
    for cur in currencies:
        print(cur, f"{{gap}}")

convert(124)

# exp output
# USD 124.00
# EUR 110.61
# JPY 17211.20
# GBP 162.32
# CHF 106.89
# CAD 163.93
# AUD 181.29
