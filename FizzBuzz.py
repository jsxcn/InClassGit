def FizzBuzz(i):
    #for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            # print ('FizzBuzz')
            return 'FizzBuzz'
        elif i % 3 == 0:
            # print ('Fizz')
            return 'Fizz'
        elif i % 5 == 0:
            # print ('Buzz')
            return 'Buzz'
        else:
            print(i)
            return i

# FizzBuzz()
