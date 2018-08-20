import math

print("Hello, let's solve square equation!")
a = float(input("Enter a:"))
b = float(input("Enter b:"))
c = float(input("Enter c:"))
equation = "{}x2+{}x+{}=0".format(a, b, c)
print(equation)
D = b**2 - 4*a*c
print("D = {}".format(D))

if D < 0:
    print("no roots")
elif D == 0:
    x = -b/(2*a)
    print("x = {}".format(x))
    left = a*x**2 + b*x + c
    print("{} = 0".format(left))
else:
    x1 = (-b+math.sqrt(D))/(2*a)
    x2 = (-b-math.sqrt(D))/(2*a)
    print("x1 = {}, x2 = {}".format(x1, x2))

