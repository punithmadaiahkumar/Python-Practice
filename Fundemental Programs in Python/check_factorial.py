#Python program to find the factorial of a number using itterative technique

num = 12
fact = 1

if num < 0: 
    print("Negative number cannot be calcaluated for factorial")
elif num == 0:
    print("Since the number is 0 then the factorial is 1")
else:

    for f in range (1,num+1):
        fact = fact*f

    print("Factorial of",num ,"is", fact)