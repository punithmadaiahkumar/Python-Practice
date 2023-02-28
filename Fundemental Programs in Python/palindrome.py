#Python script to check if a string is palindrome or not!

seq = "malayalam"
rev = seq[::-1]

if rev == seq:
    print ("The string is a palindrome")
else:
    print("The string is not palindrome")