def myfun(x):
    n = 2
    p = 1
    while n < x:
        if x % n == 0:
            print(x, "is not prime")
            p = 0
            n = x
        else:
            n += 1
    else:
        if p == 1:
            print(x, "is prime")
x = int(input("enter a number: "))
myfun(x)