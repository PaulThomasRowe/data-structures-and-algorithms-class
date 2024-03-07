# We're going to write a method that looks for numbers divisible by 3 and prints fizz, divisible by 5 and prints buzz, or divisible by 3 and 5 and prints fizzbuzz. If none of the criteria are met, the number will be printed. The method should accept a number and evalute if 1 through n meet this criteria.





def fizzbuzz(n):
    
    for i in range (1, n+1):
        if (i % 3 == 0 and i % 5 == 0):
            print ("fizzbuzz")
        elif i % 3 == 0:
            print ("fizz")
        elif i % 5 == 0:
            print ("buzz")
        else:
            print(i)



fizzbuzz(100)


