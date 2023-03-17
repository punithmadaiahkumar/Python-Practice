def func1(word):
    return word.lower()

def func2(word):
    return word.upper()

def grtfunc(funct):
    grt = funct("""hello""")
    print(grt)

grtfunc(func1)
grtfunc(func2)