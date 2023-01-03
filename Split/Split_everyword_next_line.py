
a="""This is a test script. This test a sample python"""
 
b=a.split(" ")
print(b)
for i in b:
    for j in b:
        if i==j:
            print(i)