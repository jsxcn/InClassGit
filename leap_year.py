# value = int(input("Enter a leap year: "))

def leapyr(n):
    if n % 400 == 0:
        return True
    if n % 100 == 0:
        return False
    if n % 4 == 0:
        return True
    return False

print(leapyr(n))

print(leapyr(2000), "leap year")
print(leapyr(1900), "leap year")