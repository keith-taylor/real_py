import fractions

x = -0.34 + 0.5j
x_type = type(x).__name__
print(x_type)

barp = True
barp_type = type(barp).__name__
print (barp_type)

third = fractions.Fraction(1,3)

print(third)
print(float(third))

third_type = type(third).__name__

print(third_type)

print(str(bin(256)[2:]))

int(23.4)
