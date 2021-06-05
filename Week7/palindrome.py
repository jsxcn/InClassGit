# s = input("enter a string : ")
def palindrome(s):
    a = s[::-1]
    if(s==a):
        return True
    else:
        return False

# print(palindrome(s))
