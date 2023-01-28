ar=[7,4,8,2,9]


for i in range(0,len(ar),1):

    for j in range(i+1,len(ar)):

        if(ar[i]<ar[j]):
            #swaping statements
            temp=ar[i]
            ar[i]=ar[j]
            ar[j]=temp

# [3,4,5]
#[4,3,5]
#[5,3,4]


# [12,11,1,4,5,6,7]

print(ar)