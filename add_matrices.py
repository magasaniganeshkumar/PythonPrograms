class Matrices:         
    def __init__(self,mat1,mat2):
        self.mat1 = mat1
        self.mat2 = mat2 

    def add_matrice(self):                     
        res = []
        for rows in range(len(self.mat1)):
            row = []
            for colm in range(len(self.mat1[0])):
                row.append(self.mat1[rows][colm]+self.mat2[rows][colm])
            res.append(row)
        print(*res , sep = '\n')

mat1 =  [[12,7,3],
         [4,5,6],
         [7,8,9]]
mat2 = [[5,8,1],
        [6,7,3],
        [4,5,9]]

add = Matrices(mat1,mat2)
add.add_matrice()
