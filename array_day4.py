# We have an array of runs . The array is [23,45,67,35,56]. Find out the highest and the lowest run

runs=[23,45,67,35,56]

n=len(runs)

max1=0

# For loop for finding out the highest run

for i in range(0,n,1):
    if(runs[i]>max1):
        max1=runs[i]

print("The highest run is",max1)


# For loop for finding the minimum run
#  23,45,67,35,56

min1=runs[0]

for j in range(0,n,1):
    if(runs[i]<min1):
        min1=ar[i]

print("The lowest run is",min1)

