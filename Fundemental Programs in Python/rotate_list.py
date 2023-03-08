#Python PRogram to rotate List using index slicing

def rotate_list(n):
    
    list1 = [23, 12, 5, 24, 23, 76, 86, 24, 86, 24, 75]
    list2 = (
        list1[len(list1)-n: len(list1)] + 
        list1[0:len(list1)-n]
             )
    print("Original List is:", list1)
    print("Rotated List is:", list2)

rotate_list(int(3))    