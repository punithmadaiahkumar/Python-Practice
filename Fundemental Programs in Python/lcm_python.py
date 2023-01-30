#LCM program using Python

def lcm(a,b):
    lcm = a
    while lcm % b != 0:
        lcm += a
    print(f"LCM of {a} and {b} us {lcm}.")

lcm(6,9)