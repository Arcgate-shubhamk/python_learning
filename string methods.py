#string methods
#exercise 1
name = input("enter your name")
# print(f"name in reverse  {name[::-1]}") 
if name:
    print(f"your name is {name}")
else:
    print("you din\'t enter anything")
#exercise 2
#name, char = input("enter name and a character:  ").split(",")
#print(f'length of name {len(name)}')
#print(f"count of character enterted:  {name.strip().lower().count(char.strip().lower())}")
#print(name.center(14, "*"))
#if you dont kmow the length
#print(name.center(len(name)+1, '*'))