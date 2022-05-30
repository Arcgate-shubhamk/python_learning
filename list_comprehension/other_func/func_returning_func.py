#  closure function
# program to calculate powers



def to_power(x):
    def calc(n):
        return n**x
    return calc

cube = to_power(3)
print(cube(2))

#square (x)(n)
print(to_power(2)(3))
