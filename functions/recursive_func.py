#func that calls itself again and again
def rec(n):
    if n:
       return n + rec(n-1)
    else:
        return 0
    
result = rec(10)
print(result)
     