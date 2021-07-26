class ScalarMultiplivation:
     def __init__(self, matrices, scalar):
         self.matrices = matrices
         self.scalar = scalar

     def mult_by_scalar(self):
        mat_new = []
        for mat1 in self.matrices:
           sub_mat=[]

           for mat2 in mat1:
              res = mat2* self.scalar
              sub_mat.append(res)
           mat_new.append(sub_mat)
        print(*mat_new , sep = '\n')

matrices = [[12,7,3],
            [4,5,6],
            [7,8,9]]
scalar = 9 
           
sca_mat = ScalarMultiplivation(matrices, scalar)
sca_mat.mult_by_scalar()