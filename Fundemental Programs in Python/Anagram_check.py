#Python program to Check if Two Strings are Anagram

s1='listen'
s2='silent'
if(sorted(s1)== sorted(s2)):
    print("The strings are anagrams")
else:
    print("The strings aren't anagrams")