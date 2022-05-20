
def is_palindrome(str):
   return str == str[::-1]
#rev = str[-1::-1]
    #if str == str[::-1]:
        #return True
    #return False


string = input("enter the string you want to check:  ")
print(is_palindrome(string))