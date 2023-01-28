# Write a program to find the sum of all the common multiples of 5 and 7 upto 1000.

# 0 ------- 1000 step 1  ---> 0,1,2,3........35,36
# check if the number is divisible by both 5 and 7
# Find the sum of it

sum=0
for i in range(0,1000,1):
    if((i%5 == 0)&(i%7 == 0)):
        print(i)
        sum=sum+i
print("Sum is",sum)

