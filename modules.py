import math


def cis(x):
    res = complex(math.cos(x) , math.sin(x))
    return res 

def w(m,n):
    return cis( (2*m*math.pi) / n)




# class Polynomial:
#     def __init__(self, coeffs):
#         self.coeffs = coeffs
    
#     def __str__(self):
#         res = ""
#         for i in range(len(self.coeffs)):
#             if i == 0:
#                 res += f"{self.coeffs[i].real} + "
#             elif i == 1:
#                 res += f"{self.coeffs[i]}x + "
#             elif i == len(self.coeffs) - 1:
#                 res += f"{self.coeffs[i]}x^{i}"
#             else:
#                 res += f"{self.coeffs[i]}x^{i} + "

#         return res
    


# class Complex:
#     # def __init__(self, real, imag):
#     #     self.real = real
#     #     self.imag = imag

#     def __init__(self, _str):
#         _str = _str.split('+')
#         self.real = float(_str[0])
#         self.imag = float(_str[1].split('i')[0])

#     def __str__(self):
#         return f"{self.real} + i{self.imag}"
    
#     def c_sum(self, other):
#         res = Complex('0+0i')
#         res.real = self.real + other.real
#         res.imag = self.imag + other.imag
    
#     def c_product(self, other):
#         res = Complex('0+0i')
#         res.real = (self.real * other.real) - (self.imag * other.imag)
#         res.imag = (self.imag * other.real) + (self.real * other.imag)
        
#         return res
    
#     def power(self, n):
#         if n == 0:
#             return Complex('0+0i')
#         elif n == 1:
#             return self
#         else:
#             b = power(self, (n/2))
#             b = b.product(b)
#             if (n % 2):
#                 b *= b.c_product(self)


# def w(i, j, n):
#     real = math.cos((2 * i * j * math.pi) / n)
#     imag = math.cos((2 * i * j * math.pi) / n)

#     return Complex(f'{real}+{imag}i')



        

