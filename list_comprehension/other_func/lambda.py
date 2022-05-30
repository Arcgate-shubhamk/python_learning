#usual func
# def odd_even(a):
#     return a%2==0

# print(odd_even(8))

#Lambda function

odd_even = lambda a : a%2==0
print(odd_even(8))

last_char = lambda s : s[-1]
print(last_char('arhit'))

func = lambda s : True if len(s)> 3 else False
print(func('arhit'))

func2 = lambda s : len(s) >3
print(func('arhit'))