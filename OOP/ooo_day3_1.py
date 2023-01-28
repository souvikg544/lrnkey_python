# Write a program to make a function that will return 0
# if a number is odd and return 1 if it is even

def odd_even(num):
    #statements
    if(num % 2 == 0):
        r=1
    else:
        r=0

    return r


n = int(input("Enter a number : "))

result = odd_even(n)

print("output = ",result)