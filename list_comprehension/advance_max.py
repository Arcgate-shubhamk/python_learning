users={
    'akshi' : {'score':90, 'age': 28 },
    'Arpita' : {'score':95, 'age': 32},
    'Arhit' : {'score':80, 'age': 3}
}

print(min(users, key = lambda items :users[items]['age']))

users2 =[
    {'name': 'Arpita', 'score':90,'age':30},
    {'name':'Akshi','score':95,'age':28},
    {'name': 'Arhit','score':92,'age':3}
]

print(max(users2, key = lambda item:item.get('score')))


