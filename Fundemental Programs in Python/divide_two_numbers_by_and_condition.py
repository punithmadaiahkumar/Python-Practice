#Function to print numbers which are divisibe by 3 or 5

def print_divisibles(n):
    for i in range(1,n):
        if i%3==0 or i%5==0:
            print(i)

print_divisibles(30)