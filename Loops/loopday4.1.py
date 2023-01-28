#Write a program to find the sum of all the
# elements divisible by both 3 and 4 between 60 and 500

sum=0

for i in range(60,500,1):
    if((i%3==0)&(i%4==0)):
        print(i)
        sum=sum+i
print("Sum of the elements: ",sum)