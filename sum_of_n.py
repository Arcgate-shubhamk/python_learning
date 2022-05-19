#sum of n natural numbers

# n=int(input("enter natural number"))
# total = 0
# i = 1
# while i <= n:
#     total+=i
#     i+=1
# print(f"sum of n natural numbers is{total}") 


#sum of digits of the number entered
num = input("enter a mutli digit number : " )
i = 0
total  = 0
while i <  len(num):
   total += int(num[i])
   i += 1
print(total)
