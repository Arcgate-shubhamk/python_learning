# l = ['num', 'asd',[1,2,3,],2,3,2.5,7,8.0]

# int_list = [str(i) for i in l if type(i) == int or type(i)==float]
# print(int_list)

def int_list(l):
    return [str(i) for i in l if type(i) ==int or type(i)==float]

l2 = ['num', 'asd',[1,2,3,],2,3,2.5,7,8.0]
print(int_list(l2))

#if else with list comprehension
nums = [1,2,3,4,5,6,7,8,9,10]
num2 = [i**2 if i%2==0 else -i for i in nums]
print(num2)


#in nested list
nested = [[ i for i in range(3)] for i in range (4)]
print(nested  )