#Python Program to Reverse the List using reverse function
lst = [1,2,3,4,5,6]

def rev_num_list(lst):
    print("List to be sent for reverse: ",lst)
    lst.reverse()
    print("---------------------------")
    print("Reverse List is:",lst)

rev_num_list(lst)