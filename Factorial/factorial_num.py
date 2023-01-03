def fact(num):
    k=1
    for i in range(1,num+1):
        print(i)
        fact=i*k
        print(fact)
       


if __name__=="__main__":
    input=12
    fact(input)
    print("factorial of :",input)