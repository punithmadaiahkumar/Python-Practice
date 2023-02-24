#Python Program to show bubble sort

def bubble_sort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
    print(array)

arr = [34,23,45,76,89,76]

bubble_sort(arr)