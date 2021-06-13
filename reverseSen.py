s = input("Enter your sentence: ")

def reverseStr(s):
    w = s.split(' ')
    reversedStr = ' '.join(reversed(w))

    return reversedStr

print(reverseStr(s))
