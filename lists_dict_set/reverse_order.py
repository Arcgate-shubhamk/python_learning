#reverse the order of elements of a list

# def rev(l):
#     l.reverse()
#     return l

#using slicing
# def  rev(l):
#      return l[::-1]

#append and pop
def rev(l):
    r_list = []
    for i in range(len(l)):
        popped=l.pop()
        r_list.append(popped)
    return r_list
     
normal=['mm', 'nn', 'bb', 'cc']
print(rev(normal))
    