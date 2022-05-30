def func(l, target):
    for pos, string in enumerate(l):
        if string == target:
            return pos
    return -1
strings = ['akshi','mohit','shubham', 'arhit', 'arpita']
print(func(strings, 'akku'))