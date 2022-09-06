
# 0 -- 10--step 2

# While loop

# while(condition):
    #statements
    #statement
    #increment or decrement

#If you have a number print all the digits of the number
# 6438
# print --->
# 8
# 3
# 4
# 6

n=int(input("Enter a number : "))

while(n>0):
    r=n%10 # Remainder
    n=n/10
    print(r)
