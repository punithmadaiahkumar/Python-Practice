def fun_generator():
    yield "Hello Python!!"
    yield "Interview"
 
 
obj = fun_generator()
 
print(type(obj))
 
print(next(obj))
print(next(obj))