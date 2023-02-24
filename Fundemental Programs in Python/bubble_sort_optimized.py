#Python program for implementation on Optimized Bubble Sort

def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False

        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        if (swapped == False):
            break

#code test
if __name__ == "__main__":
    arr = [45,56,43,76,23,12,87,54]

    bubblesort(arr)
    print("Sorted Array is:")
    print(arr)
    # for i in range(len(arr)):
    #     print("%d" % arr[i], end=" ")