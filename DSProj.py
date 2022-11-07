import modules as dft

n = int(input("Enter n: "))

init_coeffs = []
res_coeffs = [0] * n
w_coeffs = []

for i in range(n):
    temp = complex(input(f"\tcoeff of x^{i}: "))
    init_coeffs.append(temp)
    w_coeffs.append(dft.w(i,n)) 

for i in range(n):
    for j in range(n):
        tmp_coeffs =[0] * n
        tmp_coeffs[j] =  init_coeffs[j] * (w_coeffs[i])**j
    res_coeffs[i] = sum(tmp_coeffs)

print(res_coeffs)





