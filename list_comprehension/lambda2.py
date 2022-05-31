# def avg(*args):
#     avg=[]
#     for pair in zip(*args): #used *as we have to unpack the tuple
#        avg.append(sum(pair)/len(pair))
#     return avg

# print(avg([1,4,3],[4,2,5],[1,3,4]))


avg=lambda *args : [sum(pair)/len(pair) for pair in zip(*args)]
print(avg([1,2,3],[2,3,4]))
