"""#exercise 1
def add_vectros(a, b):
    c = []
    d = len(a)
    i = 0
    while d > i:
        c.append(a[i] + b[i])
        i += 1
    return c

print(add_vectros([1,2,3,4], [1,2,3,4]))

#exersice 2
def scalar_mult(s, v):
    c = []
    i = 0
    while len(v) > i:
        c.append(s * v[i])
        i += 1
    
    return c

print(scalar_mult(3, [1,2,3]))
#exercise 3
def dot_product(u, v):
    i = 0
    c = 0
    while len(u) > i:
        c += u[i] * v[i]
        i += 1
    return c

print(dot_product([1,2], [1,2]))

#exercise 4
import numpy as np
def copy_matrix(m):
    
    c = m
    return c
print(copy_matrix(m = [[1,2],[3,4]]))"""

#exercise 5

def add_row(matrix):
    