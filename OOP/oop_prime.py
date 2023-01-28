def prime_function(a):
    control = 0
    for i in range(2, a, 1):
        if (a % i == 0):
            control = 1
            break

    if (control == 1):
        print("Not a Prime Number")
    else:
        print("Its a Prime Number")

def prime_function_new(a):
    control = 0
    for i in range(2, a, 1):
        if (a % i == 0):
            control = 1
            break

    if (control == 1):
        return False
    else:
        return True


n=int(input("Enter a number to check for prime : "))

result = prime_function_new(n)
print(result)

