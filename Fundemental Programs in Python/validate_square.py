'''
We have provided number 36 to the `valid_square()` function. 

    By taking the square root of the number, we get 6.
    By converting it into an integer, we get 6.
    Then, take the square of 6 and get 36.
    36 is equal to the number, so the function will return True. 

'''
def valid_square(num):
    square = int(num**0.5)
    check = square**2==num
    print(num,"square validation is",check)

valid_square(10)
# False
valid_square(36)
# True