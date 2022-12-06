# Catching Info Exception:

import sys

randomList = ['a', 0, 4]

print("Random List is:", randomList)

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("Moving to next entry from the ramdom List.")
        print()
print("The reciprocal of", entry, "is", r)