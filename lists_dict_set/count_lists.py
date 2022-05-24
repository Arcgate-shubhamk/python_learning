#count the number of lists in the list provided

def count_list(l):
    count = 0
    for i in l:
        if type(i) == list:
            count += 1
    return count

given_list=[1,3,[4,5,6],[6],[7,6,4],[8,9],7 ,8 , [9,8,0]]
print(count_list(given_list))