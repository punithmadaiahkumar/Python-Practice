#Python program for Strong Number
#A strong number is a number in which the sum of the factorials of its digits is equal to the number itself. For example, 145 is a strong number because 1! + 4! + 5! = 1 + 24 + 120 = 145.

sum=0
num=145
temp=num
while(num):
    i=1
    fact=1
    r=num%10
    while(i<=r):
        fact=fact*i
        i=i+1
    sum=sum+fact
    num=num//10
if(sum==temp):
    print("Strong number")
else:
    print("Not a Strong number")