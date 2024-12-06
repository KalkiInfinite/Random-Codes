# Post Lab Questions
# a)
z = 28 % 6
print("The remainder is:", z)

x = 28 // 6
print("The quotient is:", x)

# b)
q = 3.45 / 1.22
print("The remainder is:", q)

# c)
print(round(3.5567))

# d)
x = 4
y = 2

z = complex(x, y)
print("The real part is ", z.real)
print("The imaginary part is ", z.imag)
print("The conjugate of 4+2j is ", z.conjugate())

def binarytodecimal(binary):
    decimal, i = 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * (2 ** i)
        binary = binary // 10
        i += 1
    print(decimal)

binarytodecimal(1100001110)
