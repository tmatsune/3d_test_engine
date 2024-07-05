from commons.settings import * 
from math_lib.vector import * 

class Matrix:
    def __init__(self, rows, cols, vals):
        self.rows = rows
        self.cols = cols
        self.vals = vals.copy()
    
    def get_col(self, col):
        res = []
        for i in range(self.rows):
            res.append(self.vals[i][col])
        return res 

    def get_row(self, row):
        res = []
        for i in range(self.cols):
            res.append(self.vals[row][i])
        return res

    def mult_matrix(self, other):
        assert self.cols == other.rows, f'MATRIX ERR MULTI {self.cols} != {other.rows}'
        res = []
        dim = [self.rows, other.cols]
        for r in range(self.rows):
            curr_row = self.get_row(r)
            res.append([])
            for c in range(other.cols):
                curr_col = other.get_col(c)
                res[r].append(self.get_dot(curr_row, curr_col))

        mat = Matrix(dim[0], dim[1], res)
        return mat
    
    def get_dot(self, l1: list, l2: list):
        assert len(l1) == len(l2), f'MATRIX ERR DOT: {len(l1)} != {len(l2)}'
        res = 0
        for i in range(len(l1)):
            res += l1[i] * l2[i]
        return res
    
    def make_proj(self, f_fov_deg, f_aspect_ratio, f_near, f_far):
        assert self.rows == 4 and self.cols == 4, f'ERR NOT 4x4 MATRIX'
        f_fov_rad = 1 / math.tan(f_fov_deg*0.5 / 180*math.pi)
        self.vals[0][0] = f_aspect_ratio * f_fov_rad
        self.vals[1][1] = f_fov_rad
        self.vals[2][2] = f_far / (f_far - f_near)
        self.vals[3][2] = (-f_far*f_near) / (f_far-f_near)
        self.vals[2][3] = 1


    def __repr__(self) -> str:
        res = ''
        for r in range(self.rows):
            res += '['
            for c in range(self.cols):
                res += str(self.vals[r][c])
                res += ' , ' if c < self.cols - 1 else ''
            res += ']'
            res += '\n'
        return res
    
def gen_mat(row, col, val=0):
    res = []
    for r in range(row):
        res.append([])
        for c in range(col):
            res[r].append(val)
    mat = Matrix(row, col, res)
    return mat
