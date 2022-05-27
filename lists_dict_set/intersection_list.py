#common elements finder function
def common(l1, l2):
    intersec = []
    for i in l1:
        if i in l2:
            intersec.append(i)
    return intersec 

print(common([1,3,4,54,2],[4,6,5,2,1,3]))
