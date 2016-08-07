a = " hello"
print(a[:]) #will print whole string
print(a[:3]) #will print upto 3rd index

a = a[0:3] +"p!" #creating a new value not modifying it, strings are immutable
print(a)
