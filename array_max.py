# Take an array as input and find the maximum number in the array

n=int(input("Length of the array : "))
ar=[]

for i in range(0,n,1):
    v=int(input("Element : "))
    ar.append(v)

print(ar)

m=0
for i in range(0,n,1):
    if(ar[i]>m):
        m=ar[i]

print("MAX ELEMENT IS : ", m)