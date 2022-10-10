char_str = input("enter a string : ") 
print("The original string is : " + str(char_str))
res = [ele.upper() if not idx % 2 else ele.lower() for idx, ele in enumerate(char_str)]
res = "".join(res)
# printing result
print("The alternate case string is : " + str(res))