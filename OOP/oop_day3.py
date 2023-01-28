
# Write a program such that it contains a function that will return
# 0 if the person is offline , 1 if the person is online.

def status(s):
    r=0
    if(s=="online"):
        r=1
    elif(s=="offline"):
        r=0
    else:
        r=-99

    return r

user_status=input("Enter your status : ")

r1=status(user_status)
print("Output : ",r1)

