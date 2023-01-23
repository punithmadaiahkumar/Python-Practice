#Armstrong Number Program In Python
# An Armstrong number is a number that is equal to the sum of its own digits raised to the power of the number of digits

#371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371.

n = 371
num_digits = len(str(n))
sum = 0
for digit in str(n):
  sum += int(digit)**num_digits
print(sum == n)