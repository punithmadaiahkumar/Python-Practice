#Prime Number Program in Python

def prime_number(n):
    is_prime = True
    if n < 2:
        is_prime = False
    else:
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break
    if is_prime:
        print("Prime")
    else:
        print("Not prime")

prime_number(5)