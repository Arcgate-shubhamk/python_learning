#guessing game
import random
x=random.randint(0,100)

user = int(input("guess the winning number"))

if x==user:
    print("YOU WIN!!")
elif x>user:
    print("too low")
elif x<user:
    print("too high")
else:
    print("wrong input")
print(f"winning number was {x}")
    