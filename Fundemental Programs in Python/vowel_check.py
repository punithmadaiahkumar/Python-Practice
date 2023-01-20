#Python program to count the number of Vowels in a String

def vowels_check(str):
    
    count = 0
    vowels = ['a','e','i','o','u']

    for i in str:
        if i in vowels:
            count += 1
    print("Your String is:", str)
    print("Number of Vowels in the string is: ",count)
    return count
    

str(vowels_check('Punith'))

