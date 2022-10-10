s = input("enter a string : ")
for i in range(0,len(s)):
    if(i%2==0):
        s = s.replace(s[i],s[i].upper())  
print(s)