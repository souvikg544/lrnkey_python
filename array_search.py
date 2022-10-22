

# Write a program to search an element through an array.ALso tell the index if the element is found
#Input  ----> [2,5,6,8,9,10] , 6
#Output ----> 6 is present in the index of 2


# Taking inputs

n=int(input("Length of the array :"))
ar=[]

for i in range(0,n,1):
    val=int(input("Element : "))
    ar.append(val)
print("The final array is ",ar)

# Taking input of the element to be searched

e=int(input("Element to be searched : "))

for i in range(0,n,1):
    if(e==ar[i]):
        print("Found in index ", i)