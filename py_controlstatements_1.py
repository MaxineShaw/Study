x = int(input("enter a number: "))
y = int(input("enter a number: "))
z = int(input("enter a number: "))
if x == y and x == z:
    print("all numbers are equal")
elif x != y and y != z:
    print("all numbers are not equal")
else:
    print("neither all equal or different")