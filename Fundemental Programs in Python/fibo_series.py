#Python Program for Fibonacci Series

n = 9 
first = 0
second = 1
series = [first,second]

if n == 0:
    print("the required fibonacci series is", first)

else:
    for i in range(0,n-2):
        num = series[i] + series[i+1]

        series.append(num)
        print(series)