class demo:
    def __init__(self,f_name, l_name,age):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.gender = "Male"

info = demo("Punith","Gowda",26)
print(info.f_name)
print(info.l_name)
print(info.age)
print(info.gender)

'''
In Python, __init__ is a function or function Object() { [native code] }. 
When a new object/instance of a class is created, this function is automatically called to reserve memory. 
The __init__ method is available in all classes.
'''