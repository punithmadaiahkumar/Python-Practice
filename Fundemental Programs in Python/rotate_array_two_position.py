#Python program that rotates an array by two positions to the right.

listt = [23, 12, 5, 24, 23, 76, 86, 24, 86, 24, 75]  

for i in range(0,2):
    temp = listt[len(listt)-1]
    #print(temp)
    for i in range(len(listt)-1,-1,-1):
        listt[i]= listt[i-1]
        listt[0]= temp
        #print(listt)

print(listt)