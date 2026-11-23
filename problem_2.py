#Swap two numbers (a) using a third variable, (b) without a third variable.

a = 2
b = 3
c = a,b = b, a
print(c) 


a = 10
b = 20

a = a + b
b = a - b
a = a - b
print("After swapping:")
print("a =", a)
print("b =", b)

a = 10
b = 20

a, b = b, a
print(a, b)

a = 10
b = 20

temp = a
a = b
b = temp

print("After swapping:")
print("a =", a)
print("b =", b)





