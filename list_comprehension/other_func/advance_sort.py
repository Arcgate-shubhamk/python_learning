guitars =[
    {'model': 'yamaha f310','price': 8400},
    {'model':'faith naptune','price':50000},
    {'model':'faith apollo venus','price':35000},
    {'model':'taylor 814ce','price':45000}
]

#sort by price
print(sorted(guitars, key = lambda d: d.get('price')))
print(sorted(guitars, key = lambda d: d['price']))