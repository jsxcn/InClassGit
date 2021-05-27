value = input("Enter a leap year: ")

def leap_year(value):
	if(value < 0):
		print("Invalid number")
	elif(value % 4 == 0 and (value % 100 != 0 or value % 400 == 0)):
		print(value) 
	else:
		print("Not Leap Year")
