n=int(input("Enter a number to check for prime : "))
control=0

for i in range(2,n,1):
    if(n % i == 0):
        control=1
        break

if (control == 1):
    print("Not a Prime Number")
else:
    print("Its a Prime Number")

