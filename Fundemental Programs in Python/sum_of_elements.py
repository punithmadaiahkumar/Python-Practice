#Python program to find the sum of elements

def arraySum(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

print(arraySum([1, 2, 3, 4, 5]))