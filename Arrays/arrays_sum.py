# Write a program to find the sum of all the elements of the array


# Find the product of all the elements of the array

#Input ----- > [3,4,5,6]

#Output -----> 3+4+5+6=
# 18

# Taking array as input

n=int(input("Number of elements in the array :"))
ar=[]

for i in range(0,n,1):
    v=int(input("Element"))
    ar.append(v)


sum1=0

for i in range(0,n,1):
    sum1=sum1+ar[i]

print(" The sum of all the elements : ",sum1)




