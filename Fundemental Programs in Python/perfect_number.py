#Python program for Perfect number
#A perfect number is a positive integer that is equal to the sum of its proper positive divisors excluding the number itself. For example, the proper positive divisors of 6 are 1, 2, and 3, which add up to 6. So 6 is a perfect number.

n = 28
sum1 = 0
for i in range(1, n):
    if(n % i == 0):
        sum1 = sum1 + i
if (sum1 == n):
    print("Perfect number")
else:
    print("Not a Perfect number")