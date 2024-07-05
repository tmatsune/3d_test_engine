from commons.settings import * 
from math_lib.matrix import * 
from math_lib.vector import * 

cube_mesh = [
    [ Vector(D4, D4, [0, 0, 0, 1]), Vector(D4, D4, [0, 1, 0, 1]), Vector(D4, D4, [1, 1, 0, 1]) ],
    [ Vector(D4, D4, [0, 0, 0, 1]), Vector(D4, D4, [1, 1, 0, 1]), Vector(D4, D4, [1, 0, 0, 1]) ],

    [ Vector(D4, D4, [1, 0, 0, 1]), Vector(D4, D4, [1, 1, 0, 1]), Vector(D4, D4, [1, 1, 1, 1]) ],
    [ Vector(D4, D4, [1, 0, 0, 1]), Vector(D4, D4, [1, 1, 1, 1]), Vector(D4, D4, [1, 0, 1, 1]) ],

    [ Vector(D4, D4, [1, 0, 1, 1]), Vector(D4, D4, [1, 1, 1, 1]), Vector(D4, D4, [0, 1, 1, 1]) ],
    [ Vector(D4, D4, [1, 0, 1, 1]), Vector(D4, D4, [0, 1, 1, 1]), Vector(D4, D4, [0, 0, 1, 1]) ],

    [ Vector(D4, D4, [0, 0, 1, 1]), Vector(D4, D4, [0, 1, 1, 1]), Vector(D4, D4, [0, 1, 0, 1]) ],
    [ Vector(D4, D4, [0, 0, 1, 1]), Vector(D4, D4, [0, 1, 0, 1]), Vector(D4, D4, [0, 0, 0, 1]) ],

    [ Vector(D4, D4, [0, 1, 0, 1]), Vector(D4, D4, [0, 1, 1, 1]), Vector(D4, D4, [1, 1, 1, 1]) ],
    [ Vector(D4, D4, [0, 1, 0, 1]), Vector(D4, D4, [1, 1, 1, 1]), Vector(D4, D4, [1, 1, 0, 1]) ],

    [ Vector(D4, D4, [1, 0, 1, 1]), Vector(D4, D4, [0, 0, 1, 1]), Vector(D4, D4, [0, 0, 0, 1]) ],
    [ Vector(D4, D4, [1, 0, 1, 1]), Vector(D4, D4, [0, 0, 0, 1]), Vector(D4, D4, [1, 0, 0, 1]) ],
]



class Cube:
    def __init__(self, app, mesh):
        self.app = app
        self.mesh = mesh
        self.test_time = 0
        self.mat_norm = gen_mat(4, 4, 1)
        self.mat_rot_z = gen_mat(4, 4)
        self.mat_rot_x = gen_mat(4, 4)
        self.mat_proj = gen_mat(4, 4)
        self.camera = Vector(4,4, [0,0,0,0])

    def render(self, surf):
        self.test_time += .2

        self.mat_rot_z.vals[0][0] = math.cos(self.test_time * .5)
        self.mat_rot_z.vals[0][1] = math.sin(self.test_time * .5)
        self.mat_rot_z.vals[1][0] = -math.sin(self.test_time * .5)
        self.mat_rot_z.vals[1][1] = math.cos(self.test_time * .5)
        self.mat_rot_z.vals[2][2] = 1
        self.mat_rot_z.vals[3][3] = 1

        self.mat_rot_x.vals[0][0] = 1
        self.mat_rot_x.vals[1][1] = math.cos(self.test_time * .5)
        self.mat_rot_x.vals[1][2] = math.sin(self.test_time * .5)
        self.mat_rot_x.vals[2][1] = -math.sin(self.test_time * .5)
        self.mat_rot_x.vals[2][2] = math.cos(self.test_time * .5)
        self.mat_rot_x.vals[3][3] = 1

        f_near = 0.1  # near plane
        f_far = 1000  # far plane
        f_fov = 90
        f_aspect_ratio = HEIGHT / WIDTH
        f_fov_rad = 1 / math.tan(f_fov*0.5 / 180*math.pi)

        self.mat_proj.vals[0][0] = f_aspect_ratio * f_fov_rad
        self.mat_proj.vals[1][1] = f_fov_rad
        self.mat_proj.vals[2][2] = f_far / (f_far - f_near)
        self.mat_proj.vals[3][2] = (-f_far*f_near) / (f_far-f_near)
        self.mat_proj.vals[2][3] = 1

        triangles = []

        for tri in self.mesh:
            trix_rot_z = copy.deepcopy((tri))
            tri_trans = copy.deepcopy((tri))

            # rot cube around z axis
            triz_res_1 = self.mult_mat_by_vec(trix_rot_z[0], 0, self.mat_rot_z)
            triz_res_2 = self.mult_mat_by_vec(trix_rot_z[1], 0, self.mat_rot_z)
            triz_res_3 = self.mult_mat_by_vec(trix_rot_z[2], 0, self.mat_rot_z)
            rot_z_vec = [Vector(D4, D4, triz_res_1), Vector(D4, D4, triz_res_2), Vector(D4, D4, triz_res_3)]

            # rot cube around x axis
            trix_res_1 = self.mult_mat_by_vec(rot_z_vec[0], 0, self.mat_rot_x)
            trix_res_2 = self.mult_mat_by_vec(rot_z_vec[1], 0, self.mat_rot_x)
            trix_res_3 = self.mult_mat_by_vec(rot_z_vec[2], 0, self.mat_rot_x)
            rot_x_vec = [Vector(D4, D4, trix_res_1), Vector(D4, D4, trix_res_2), Vector(D4, D4, trix_res_3)]
            
            # translate cube away form screen 
            tri_trans = copy.deepcopy((rot_x_vec))
            tri_trans[0].points[2] = rot_x_vec[0].points[2] + 3
            tri_trans[1].points[2] = rot_x_vec[1].points[2] + 3
            tri_trans[2].points[2] = rot_x_vec[2].points[2] + 3


            vec1 = Vector(3,3,[0,0,0])
            vec1.points[0] = tri_trans[1].points[0] - tri_trans[0].points[0]
            vec1.points[1] = tri_trans[1].points[1] - tri_trans[0].points[1]
            vec1.points[2] = tri_trans[1].points[2] - tri_trans[0].points[2]

            vec2 = Vector(3, 3, [0, 0, 0])
            vec2.points[0] = tri_trans[2].points[0] - tri_trans[0].points[0]
            vec2.points[1] = tri_trans[2].points[1] - tri_trans[0].points[1]
            vec2.points[2] = tri_trans[2].points[2] - tri_trans[0].points[2]

            normal = Vector(3,3,[0, 0, 0])
            normal.points[0] = vec1.points[1] * vec2.points[2] - vec1.points[2] * vec2.points[1]
            normal.points[1] = vec1.points[2] * vec2.points[0] - vec1.points[0] * vec2.points[2]
            normal.points[2] = vec1.points[0] * vec2.points[1] - vec1.points[1] * vec2.points[0]

            ln = math.sqrt(normal.points[0]*normal.points[0] + normal.points[1]*normal.points[1] + normal.points[2]*normal.points[2])
            if ln != 0:
                normal.points[0] /= ln
                normal.points[1] /= ln
                normal.points[2] /= ln

            normal_dot = normal.points[0]*(tri_trans[0].points[0] - self.camera.points[0]) + \
                normal.points[1]*(tri_trans[0].points[1] - self.camera.points[1]) + \
                normal.points[2]*(tri_trans[0].points[2] - self.camera.points[2])
            
            if normal_dot < 0:

                # shading, light assumes that if z is facing player, that side will be more white 
                # get the dot product of the light and the normal to see how similar the vector are
                # the more similar the vectors, the more the light is hitting the side of the cube
                light_vec = Vector(3, 3, [0,0,-1])
                light_vec = light_vec.normalize()
                light_dot = light_vec.dot(normal)

                face_col = [255, 255, 255]
                for i in range(3): face_col[i] *= light_dot
                col = (face_col[0], face_col[1], face_col[2])

                # mult by projection matrix 
                tri_res_1 = self.mult_mat_by_vec(tri_trans[0], 0, self.mat_proj)
                tri_res_2 = self.mult_mat_by_vec(tri_trans[1], 0, self.mat_proj)
                tri_res_3 = self.mult_mat_by_vec(tri_trans[2], 0, self.mat_proj)
                vecs = [tri_res_1, tri_res_2, tri_res_3, col]

                vecs[0][0] += 1
                vecs[0][1] += 1
                vecs[1][0] += 1
                vecs[1][1] += 1
                vecs[2][0] += 1
                vecs[2][1] += 1

                vecs[0][0] *= .4 * WIDTH
                vecs[0][1] *= .4 * HEIGHT
                vecs[1][0] *= .4 * WIDTH
                vecs[1][1] *= .4 * HEIGHT
                vecs[2][0] *= .4 * WIDTH
                vecs[2][1] *= .4 * HEIGHT

                triangles.append(vecs)

        triangles = sorted(triangles, key=lambda x: self.dist(tri))
        for tri in triangles:
            self.render_tri(surf, tri, tri[3])
    
    def dist(self, tri):
        f1 = (tri[0].points[2] + tri[1].points[2] + tri[2].points[3]) / 3
        return f1

    def update(self):
        print('testing cube')

        f_near = 0.1 # near plane
        f_far = 1000 # far plane
        f_fov = 90
        f_aspect_ratio = HEIGHT / WIDTH
        
        self.mat_proj.make_proj(f_fov, f_aspect_ratio, f_near, f_far)

        for tri in self.mesh:
            tri_proj = copy.deepcopy((tri))
            tri_res = self.mult_mat_by_vec(tri_proj[0], 0, self.mat_proj)
            #self.render_tri(surf, tri_res)

    def mult_mat_by_vec(self, in_vec, out_vec, mat):
        res = [0,0,0,0]
        res[0] = in_vec.points[0] * mat.vals[0][0] + in_vec.points[1] * mat.vals[1][0] + in_vec.points[2] * mat.vals[2][0] + mat.vals[3][0]
        res[1] = in_vec.points[0] * mat.vals[0][1] + in_vec.points[1] * mat.vals[1][1] + in_vec.points[2] * mat.vals[2][1] + mat.vals[3][1]
        res[2] = in_vec.points[0] * mat.vals[0][2] + in_vec.points[1] * mat.vals[1][2] + in_vec.points[2]  * mat.vals[2][2] + mat.vals[3][2]
        w = in_vec.points[0] * mat.vals[0][3] + in_vec.points[1] * mat.vals[1][3] + in_vec.points[2] * mat.vals[2][3] + mat.vals[3][3]
        if w != 0:
            res[0] /= w
            res[1] /= w
            res[2] /= w
        return res

    def render_tri(self, surf, ps, col):
        pg.draw.polygon(surf, col, [(ps[0][0], ps[0][1]), (ps[1][0], ps[1][1]), (ps[2][0], ps[2][1])], 0)
        pg.draw.polygon(surf, BLACK, [(ps[0][0], ps[0][1]), (ps[1][0], ps[1][1]), (ps[2][0], ps[2][1])], 1)

    def __repr__(self) -> str:
        f = ''
        for i in range(len(self.mesh)):
            for j in range(len(self.mesh[0])):
                f += '['
                for k in range(len(self.mesh[0][0].points)):
                    f += str(self.mesh[i][j].points[k]) + ", "
                f += ']'
            f += '\n'
        return f
