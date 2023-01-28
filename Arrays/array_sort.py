# [7,4,8,2,9]  ----> Sort this array in ascending order --->[2,4,7,8,9]

# Selection sort

ar=[7,4,8,2,9]


for i in range(0,len(ar),1):

    for j in range(i+1,len(ar)):

        if(ar[i]>ar[j]):
            #swaping statements
            temp=ar[i]
            ar[i]=ar[j]
            ar[j]=temp

print(ar)



