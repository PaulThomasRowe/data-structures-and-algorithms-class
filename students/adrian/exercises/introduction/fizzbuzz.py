# We are going to define paramaters divisible by 3, and print fizz, divisible by 5 and print buzz, divisible by 3 and 5 and print fizzbuzz. If a variable is not divisible by either, we will print the number

def fizzbuzz(n):
    for i in range (1, n+1):
        if (i % 3 == 0 and i % 5 == 0):
            print("fizzbuzz")
        elif i % 3 == 0:
            print ("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)


fizzbuzz(100)
