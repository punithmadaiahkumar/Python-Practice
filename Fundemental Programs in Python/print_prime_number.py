#Python program to print all prime numbers up to n

def prime_numbers(n):
    for i in range(2, n+1):
        if (n % i) == 0:
            print(i, end = " ")

prime_numbers(50)