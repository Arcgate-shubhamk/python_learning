#watch coco
name, age = input("please enter your name and age").split(" ")
if name[0] == "a" or name[0] == "A" and int(age) >=10:
    print("enjoy watching coco")
else:
    print("sorry you can't watch it")