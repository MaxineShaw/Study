x = int(input("enter a number: "))
y = int(input("enter a number: "))
z = int(input("enter a number: "))
if x < y < z:
    print("Increasing order")
elif x > y > z:
    print("Decreasing order")
else:
    print("Neither increasing or decreasing order")