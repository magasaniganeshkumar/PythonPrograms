class MatrixVector:
     def __init__(self, matrices, vector):
         self.matrices = matrices
         self.vector = vector

     def mult_by_vector(self):
        result = []
        total = 0
        for row in range(len(self.matrices)):
           res = self.matrices[row]
           for colm in range(len(self.vector)):
              total += res[colm] * self.vector[colm]
           result.append(total)
    
        print(result)

matrices = [[5,1,3],
            [1,1,1],
            [1,2,1]]
vector = [1,2,3] 
           
vec_mat = MatrixVector(matrices, vector)
vec_mat.mult_by_vector()