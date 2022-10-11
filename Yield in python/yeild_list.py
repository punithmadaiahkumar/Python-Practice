# generator to print even numbers
def print_even(yield_list):
    for i in yield_list:
        if i % 2 == 0:
            yield i
 
# initializing list
yield_list = [1, 4, 5, 6, 7, 8, 9]
 
# printing initial list
print("The original list is : " + str(yield_list))
 
# printing even numbers
print("The even numbers in list are : ", end=" ")
for j in print_even(yield_list):
    print(j, end=" ")