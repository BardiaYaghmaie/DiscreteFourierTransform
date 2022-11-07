import modules as dft
init_coeffs = []
res_coeffs = []
w_coeffs = []

n = int(input("Enter n: "))

for i in range(n):
    temp = complex(input(f"\tcoeff of x^{i}: "))
    init_coeffs.append(temp)
    w_coeffs.append(dft.w(i,n)) 

for i in range(n):
    for j in range(n):
        tmp_coeffs =[]
        tmp_coeffs[j] =  init_coeffs[j] * (w_coeffs[i])**j
    res_coeffs[i] = sum(tmp_coeffs)

print(res_coeffs)





