age = int(input('enter your age:'))
if 0<age<=3:
    print("FREE ENTRY")
elif 3<age<=10:
    print("pay 150")
elif 10<age<=60:
    print("pay 250")
elif age>60:
    print("pay 200")
else:
    print("error")
    