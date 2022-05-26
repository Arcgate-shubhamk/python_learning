def outer(a,b):
    def inner(a,b):
        return a+b
    
    add=inner(a,b)
    return add + 5    

x = int(input("enter a: "))
y = int(input("enter b: "))
print(outer(x,y))
