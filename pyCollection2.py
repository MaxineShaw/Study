sample = [20, 30, 25, 35, -16, 60, -100]
z = 0
x = 0
while x <= 6:
    n = sample[x]
    y = n + z
    z = y
    avg = z / len(sample)
    x += 1
else:
    print(avg)