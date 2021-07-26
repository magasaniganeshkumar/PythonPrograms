class TransposeMatrix:
      def __init__(self, matrices):
         self.matrices = matrices

      def mat_transpose(self):
         rows = len(self.matrices)
         columns = len(self.matrices[0])

         res_matrix = []
         for j in range(columns):
            row = []
            for i in range(rows):
               row.append(self.matrices[i][j])
            res_matrix.append(row)

         print(*res_matrix, sep = '\n')

matrices = [[5,8,1],
            [6,7,3],
            [4,5,9]]
           
tran_mat = TransposeMatrix(matrices)
tran_mat.mat_transpose()