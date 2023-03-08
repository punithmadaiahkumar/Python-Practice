#Python program to Randomize the elements of a list while it's running

import random

list1 = ['This', 'is', 'Python', 'list', 'randomize']
print("Original List is: ",list1)

random.shuffle(list1)
print("After Ramdomize: ",list1)
