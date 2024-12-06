x1, x2 = input("Enter no: ").split(",")
y1, y2 = input("Enter no: ").split(",")

dist = (((int(x2) - int(x1)) ** 2) + ((int(y2) - int(y1)) ** 2)) ** 0.5
print("The distance between two points is:", dist)
