l = 67
a = int((l-1)/2)

for x in range(a,0,-1):
    y = (l-2*x)
    print(" " * x,end="")
    print("*" * y)
print (" " * a, end="")
print("|")