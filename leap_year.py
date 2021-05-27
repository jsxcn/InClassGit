value = int(input("Enter a leap year: "))

def leap_year(n):
	if(n < 0):
		print(n, "invalid number")
	elif(n % 4 == 0 and (n % 100 != 0 or n % 400 == 0)):
		print(n, "is a leap year") 
	else:
		print(n, "not Leap Year")

leap_year(value)