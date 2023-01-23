#remove vovels from string

s = 'Punith' 
vowels = ['a', 'e', 'i', 'o', 'u']
newStr = ''
for i in s:
  if i not in vowels:
    newStr += i
print(newStr)