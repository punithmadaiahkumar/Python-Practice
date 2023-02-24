#Python code to determine if a given number is binary or not!

num = 1101001  

while(num > 0):
    i = num % 10
    if i !=0 and i != 1:
        print(" Given number is not Binary")
    break

num = num // 10

if num == 0:
    print("Given number is Binary")