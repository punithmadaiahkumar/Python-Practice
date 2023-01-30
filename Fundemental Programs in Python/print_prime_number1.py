#Python program to print all prime numbers up to n
n = 10
for i in range(2, n+1):
  is_prime = True
  for j in range(2, i):
    if i % j == 0:
      is_prime = False
      break
  if is_prime:
    print(i)