numarray = list()
num = input("enter the string of numbers: ")

def calculate_sum(num, target_sum):
    for(i = 0; i < len(num); i++):
        for(j = i + 1; j < len(num); j++):
            if(num[i] + num[j] == target_sum):
                print("result -" + "[]" + i + ", " + j + "]")
                return target_sum
