from commons.settings import * 

class Space(Enum):
    ZEROD = 0,
    ONED = 1,
    TWOD = 2,
    THREED = 3,
    FOURD = 4

D1 = 1
D2 = 2
D3 = 3
D4 = 4

class Vector:
    def __init__(self, space, size, points):
        self.space = space
        self.size = size
        self.points = points.copy()
        self.x = points[0] if self.size > 0 else inf
        self.y = points[1] if self.size > 1 else inf
        self.z = points[2] if self.size > 2 else inf
        self.w = points[3] if self.size > 3 else inf
    
    def copy(self):
        return Vector(self.space, self.size, self.points)

    def dot(self, other):
        assert self.space == other.space, f'VEC SPACE ERR: {self.space} != {other.space}'
        res = 0 
        for i in range(self.space): res += self.points[i] * other.points[i]
        return res  
    
    def cross_product(self, other):
        res = Vector(self.space, self.size, gen_vec(3))

    def normalize(self):
        res = Vector(self.space, self.size, self.empty_array())
        total = 0
        for p in self.points: total += pow(p,2)
        total = math.sqrt(total)
        for i in range(self.space):
            res.points[i] = self.points[i] / total
        return res
            
    def empty_array(self):
        res = []
        for i in range(self.size): res.append(0)
        return res

    def __repr__(self) -> str:
        res = '<'
        for i in range(self.size):
            res += ' ' + str(self.points[i])
            res += ',' if i < self.size - 1 else ' '
        res += '>'
        return res

def gen_array(size, val):
    res = []
    for i in range(size): res.append(val)
    return res

def gen_vec(space, val=0):
    return Vector(space, space, gen_array(space, val))

def sub_vectors(v1: Vector, v2: Vector):
    assert v1.space == v2.space, f'ERR VEC SPACE, {v1.space} != {v2.space}'
    LN = v1.space
    res_vec: Vector = gen_vec(LN)
    for i in range(LN): res_vec.points[i] = v1.points[i] - v2.points[i]
    return res_vec

def add_vectors(v1: Vector, v2: Vector):
    assert v1.space == v2.space, f'ERR VEC SPACE, {v1.space} != {v2.space}'
    LN = v1.space
    res_vec: Vector = gen_vec(LN)
    for i in range(LN): res_vec.points[i] = v1.points[i] - v2.points[i]
    return res_vec

def vector_length(v1):
    total = 0 
    for i in range(v1.space): total += math.pow(v1.points[i], 2)
    return math.sqrt(total)
