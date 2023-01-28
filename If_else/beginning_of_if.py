# Write a program to check whether a person is adult or not.
# Child--teenager--adult--senior citizen

age=int(input("Enter your age : "))

# elif -----> else if -----> what should I do if the if is not satisfying

if(age<=12):
    print("Child")

elif((age>12) & (age<=18)):
    print("Teenager")

elif((age>18) & (age<60)):
    print("Adult")

# Else denotes that all the conditions are not being satisfied

else:
    print("Senior citizen")