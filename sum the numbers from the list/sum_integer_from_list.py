a=[123, 456, 789]
b=[]
#[6,19,12]

for i in a:
    stf=0
    for j in str(i):
        stf+=int(j)
    b.append(stf)
print(b)