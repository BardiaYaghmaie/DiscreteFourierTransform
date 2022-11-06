#! usr/bin/env python3
import modules as m

a_poly_coeffs = []
n = int(input("Enter n:"))

print(f"Enter {n} numbers as coefficients of polynomial: ")

for i in range(n):
    tmp = m.Complex(input())
    a_poly_coeffs.append(tmp)
    
b_poly_coeffs = []

for i in range(n):
    x = m.Complex('0+0i')
    for j in range(n):
        w = m.w(i, j, n)
        # x += a_poly_coeffs[j] * w
        x = x.c_sum(a_poly_coeffs[j].c_product(w))

    b_poly_coeffs.append(x)

print(b_poly_coeffs[0])






