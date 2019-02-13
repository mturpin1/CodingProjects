cart_prices = [12.34,
    23.45,
    34.56,
    45.67,
    67.89,
    78.90,
    43.21,
    54.32,
    65.43,
    76.54
]
for price in cart_prices:
    if price > 25:
        print(f'The {price} item is too expensive.')
    else:
        print(f'The {price} item is affordable.')

for x in range(0, 15):
    print('Hello World')