from commons.settings import * 
from math_lib.matrix import * 
from math_lib.vector import * 
from scripts.cube import *

m1 = [
    [2,1],
    [1,2],
    [4,0]
]

m2 = [
    [7],
    [10],
]

mat1 = Matrix(3, 2, m1)
mat2 = Matrix(2, 1, m2)
res = mat1.mult_matrix(mat2)
print(res)



