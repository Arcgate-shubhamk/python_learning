#square of the elements of a list
def sq_list(l):
    square=[]
    for i in l:
        square.append(i**2)
    return square


numbers = list(range(1,6))
print(sq_list(numbers))
             