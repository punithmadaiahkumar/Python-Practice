#HCF program in python


def hcfs(a,b):
    if a > b:
        smaller = b
    else:
        smaller = a
    for i in range(1,smaller+1):
        if (a%i == 0) and (b%i == 0):
            hcf = i
    print(f"HCF of {a} and {b} is {hcf}")

hcfs(15,20)