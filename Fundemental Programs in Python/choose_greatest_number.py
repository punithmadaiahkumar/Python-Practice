#Python program to find the greatest of three numbers
def greatest(a,b,c):
    if a>b and a>c:
        print("The greatest of three numbers is",a)
    elif b>a and b>c:
        print("The greatest of three numbers is",b)
    elif c>a and c>b:
        print("The greatest of three numbers is",c)

greatest(70,59,80)