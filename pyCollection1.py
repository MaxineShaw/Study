sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
x = 0
z = 0
while x <=9:
    n = sample[x]
    y = n + z
    z = y
    x += 1
else:
    print(z)