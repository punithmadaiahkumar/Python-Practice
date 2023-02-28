#Print Numbers in a Range Without using Loops
def printno(upper):
    if(upper>0):
        printno(upper-1)
        print(upper)
printno(10)