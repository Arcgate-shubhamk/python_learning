#count the characters of string entered
#algorithm
# 1. enter name
# 2. sort unique characters
# 3. count the string chararcters


name = input("enter your name")

temp_var = ""
i = 0
while i < len(name):
    if name[i]  not in temp_var:
        temp_var += name[i]
        print(f" {name[i]} : {name.count(name[i])}")
    i += 1
     