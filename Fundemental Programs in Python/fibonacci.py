#Fibonacci Series program  
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
        print(a)

fibonacci(10)
