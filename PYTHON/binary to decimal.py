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
