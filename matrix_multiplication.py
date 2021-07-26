class Matrices:         
    def __init__(self,mat1,mat2):
        self.mat1 = mat1
        self.mat2 = mat2 

    def multi_matrice(self):                     
        responce = []
        result = []
        for i in range(len(self.mat1)):
           for j in range(len(self.mat2[0])):
              sums=0
              for k in range(len(self.mat2)):
                  sums=sums+(self.mat1[i][k]*self.mat2[k][j])
              responce.append(sums)
           result.append(responce)
           responce = []

        print(*result , sep = '\n')

mat1 =  [[12,7,3],
         [4,5,6],
         [7,8,9]]
mat2 = [[5,8,1],
        [6,7,3],
        [4,5,9]]

multi = Matrices(mat1,mat2)
multi.multi_matrice()
