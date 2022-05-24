#filter odd even

def num(l):
    even=[]
    odd=[]
    for i in l:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    output = [odd, even]
    return output

numbers=[23,42,61,53,72,81,28,90,12]
print(num(numbers))