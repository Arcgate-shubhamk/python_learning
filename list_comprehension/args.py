def power_of(num, *args):
   if args:
       return [i**num for i in args]
   else:
       return "you didn't passed any arguments"
 
nums = [1,2,3]  
print(power_of(3  , *nums))