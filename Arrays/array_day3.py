# Take an array as input , and return all the elements of the array to the power 3 (
# return cube of the elements

# Input ---> [2,4,5,,6]
# Output -----> [8,64,125,216]

ar=[]

n=int(input("Length of the array : "))
# -------------n
v=0

for i in range(0,n,1):
    v=int(input("Element : "))
    ar.append(v)

print("Original Array :")
print(ar)

for j in range(0,n,1):
    ar[j]=ar[j]**3

print("Modified Array :")
print(ar)