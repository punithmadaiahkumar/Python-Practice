#Python program to find the average of all elements

def average(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum / len(arr)
print(average([12, 22, 32, 42, 52]))