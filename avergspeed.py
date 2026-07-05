#Three cyclists are riding at the speed of 10,20,30 km/h. Find the average and compare which cyclist is riding slower than the average speed?
a = int(input("enter a value:"))
b = int(input("enter a value 2:"))
c = int(input("enter a value 3:"))

avg = (a + b + c) / 3
print("avg =", avg)

if avg > a and avg > b and avg > c:
    print("%d is higher that %d and %d" % (avg, a, b, c))
elif avg > a and avg > b:
    print("%d is higher than %d, %d" % (avg, a, b))
elif avg > a and avg > c:
    print("%d is higher than %d, %d" % (avg, a, c))
elif avg > b and avg > c:
    print("%d is higher than %d, %d" % (avg, b, c))
elif avg > a:
    print("%d is higher than %d" % (avg, a))
elif avg > b:
    print("%d is higher than %d" % (avg, b))
elif avg > c:
    print("%d is higher than %d" % (avg, c))
else:
    print("invalid input")

    